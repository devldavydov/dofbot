import tempfile
from pathlib import Path

import telebot

from dofbot.dofcalculator.dofcalculator import DofCalculator
from dofbot.dofcalculator.exceptions import DofCalculatorInvalidQuery
from dofbot.htmlbuilder.htmlbuilder import HtmlBuilder
from dofbot.htmlbuilder.elements import Header


class DofBot:
    def __init__(self, token: str):
        self._bot = telebot.TeleBot(token, parse_mode=None)
        self._register_handlers()

    def start(self):
        self._bot.infinity_polling()

    def _register_handlers(self) -> None:
        @self._bot.message_handler(commands=['start'])
        def _start_handler(message: telebot.types.Message) -> None:
            self._process_start(message)

        @self._bot.message_handler()
        def _process_query(message: telebot.types.Message) -> None:
            self._process_query(message)

    def _process_start(self, message: telebot.types.Message) -> None:
        msg = 'Hello, my friend!\n'
        msg += 'This is Depth Of Field calculation Bot!\n\n'
        msg += 'Use query language to calculate DoF in formats:\n'
        msg += '<b>FL=&lt;focal length in mm&gt;</b>\n'
        msg += 'Returns DoF table for this focal length with predefined list of apertures and focus distances\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,F=&lt;aperture number&gt;</b>\n'
        msg += 'Returns DoF table row for this focal length and aperture\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,FD=&lt;focus distance [m]&gt;</b>\n'
        msg += 'Returns DoF table column for this focal length and focus distance\n\n'
        msg += '<b>FL=&lt;focal length [mm]&gt,F=&lt;aperture number&gt,FD=&lt;focus distance [m]&gt;</b>\n'
        msg += 'Returns DoF table cell value for this focal length, aperture and focus distance\n\n'
        msg += 'Send query via message and get html result with DoF calculation'
        self._bot.send_message(message.chat.id, msg, parse_mode='html')

    def _process_query(self, message: telebot.types.Message) -> None:
        try:
            dof_calc = DofCalculator.from_query(message.text)
        except DofCalculatorInvalidQuery:
            self._bot.send_message(message.chat.id, '<b>Wrong query!</b>')
            return

        bldr = HtmlBuilder()
        bldr.add_element(Header('Depth Of Field Calculation', 1))
        bldr.add_element(Header(f'Focal length = {dof_calc.focal_length}'))
        bldr.add_element(Header(f'Aperture = {dof_calc.aperture}'))
        bldr.add_element(Header(f'Focus distance = {dof_calc.focus_distance}'))

        with tempfile.TemporaryDirectory() as tmp_dir:
            result_file = Path(tmp_dir) / 'calculation.html'
            with result_file.open('w+') as f:
                f.write(bldr.build())
                f.seek(0)
                self._bot.send_document(message.chat.id, f)
