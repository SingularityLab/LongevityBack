```python
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import TELEGRAM_API_TOKEN
from bot_handlers import handle_message, start, help_command, add_test_result, consult

def main() -> None:
    updater = Updater(token=TELEGRAM_API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("add_test_result", add_test_result))
    dispatcher.add_handler(CommandHandler("consult", consult))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
```