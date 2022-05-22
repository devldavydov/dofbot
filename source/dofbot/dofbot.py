import telebot


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

    def _process_start(self, message: telebot.types.Message) -> None:
        msg = f'Hello, my friend!\n'
        msg += 'This is Depth Of Field calculation Bot!\n'
        msg += 'See you soon!'
        self._bot.send_message(message.chat.id, msg, parse_mode='html')
