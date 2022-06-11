import logging
import tempfile
from pathlib import Path

import telebot

from dofbot.dofcalculator.exceptions import DofCalculatorInvalidQuery
from dofbot.dofqueryprocessor import DofQueryProcessor

logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s', encoding='utf-8', level=logging.INFO)


class DofBot:
    def __init__(self, token: str):
        self._bot = telebot.TeleBot(token, parse_mode=None)
        self._register_handlers()
        self._logger = logging.getLogger(__name__)

    def start(self):
        self._logger.info('Bot started')
        self._bot.infinity_polling()

    def _register_handlers(self) -> None:
        @self._bot.message_handler(commands=['start'])
        def _start_handler(message: telebot.types.Message) -> None:
            self._process_start(message)

        @self._bot.message_handler()
        def _process_query(message: telebot.types.Message) -> None:
            self._process_query(message)

    def _process_start(self, message: telebot.types.Message) -> None:
        self._logger.info(f'Received [start] command from {self._get_user_log_info(message)}')
        msg = 'Hello, my friend!\n'
        msg += 'This is Depth Of Field calculation Bot for FF camera!\n\n'
        msg += 'Use query language to calculate DoF in formats:\n'
        msg += '<b>FL=&lt;focal length in mm&gt;</b>\n'
        msg += 'Returns DoF table for this focal length with predefined list of f-numbers and focus distances\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,FN=&lt;aperture f-number&gt;</b>\n'
        msg += 'Returns DoF table row for this focal length and f-number\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,FD=&lt;focus distance [m]&gt;</b>\n'
        msg += 'Returns DoF table column for this focal length and focus distance\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,FN=&lt;aperture f-number&gt,FD=&lt;focus distance [m]&gt;</b>\n'
        msg += 'Returns DoF table cell value for this focal length, f-number and focus distance\n\n'
        msg += 'Send query via message and get html result with DoF calculation'
        self._bot.send_message(message.chat.id, msg, parse_mode='html')

    def _process_query(self, message: telebot.types.Message) -> None:
        query = message.text
        user_log_info = self._get_user_log_info(message)

        self._logger.info(f'Received query [{query}] from {user_log_info}')
        try:
            dof_calc_result = DofQueryProcessor(query).process()
        except DofCalculatorInvalidQuery:
            self._bot.send_message(message.chat.id, '<b>Wrong query!</b>', parse_mode='html')
            self._logger.error(f'Wrong query from {user_log_info}')
            return
        except Exception:
            self._bot.send_message(message.chat.id, '<b>Internal error!</b>', parse_mode='html')
            self._logger.exception(f'Exception when processing query from {user_log_info}')
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            result_file = Path(tmp_dir) / 'calculation.html'
            with result_file.open('w+') as f:
                f.write(dof_calc_result)
                f.seek(0)
                self._bot.send_document(message.chat.id, f)
                self._logger.info(f'Send result on query from {user_log_info}')

    @staticmethod
    def _get_user_log_info(message: telebot.types.Message) -> str:
        return f'[User(id={message.from_user.id}, username={message.from_user.username}), Chat(id={message.chat.id})]'
