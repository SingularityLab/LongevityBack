```python
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from .config import TELEGRAM_API_TOKEN, OPENAI_API_KEY
from .ai_module import generate_advice
from .database_module import add_user, add_test_result, get_user, get_test_results
from .models.user import User
from .models.test_results import TestResults
from .utils import validate_test_results

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = get_user(user_id)
    if not user:
        add_user(User(id=user_id))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to HealthBot! Type /help for commands.")

def help(update: Update, context: CallbackContext):
    help_text = """
    /start - Start the bot
    /help - Show this help message
    /add_test_result - Add your test results
    /consult - Get health advice based on your test results
    """
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def add_test_result(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    test_results = update.message.text.split()[1:]
    if validate_test_results(test_results):
        add_test_result(TestResults(user_id=user_id, results=test_results))
        context.bot.send_message(chat_id=update.effective_chat.id, text="Test results added successfully.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid test results. Please try again.")

def consult(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    test_results = get_test_results(user_id)
    if test_results:
        advice = generate_advice(test_results)
        context.bot.send_message(chat_id=update.effective_chat.id, text=advice)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No test results found. Please add your test results first.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == '/start':
        start(update, context)
    elif text == '/help':
        help(update, context)
    elif text.startswith('/add_test_result'):
        add_test_result(update, context)
    elif text == '/consult':
        consult(update, context)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Unknown command. Type /help for commands.")

def error(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="An error occurred. Please try again.")

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
add_test_result_handler = MessageHandler(Filters.regex('^/add_test_result .*'), add_test_result)
consult_handler = CommandHandler('consult', consult)
message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
error_handler = MessageHandler(Filters.command, error)
```