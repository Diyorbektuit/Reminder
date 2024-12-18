from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters

from .start import start
from .add import start_add_reminder, get_title, get_text, get_date
from .list import list_reminders
from .login import login_username, login_password, cancel, logout, check_credentials
from .done import done_reminders, done_reminders_2


reminder_done_handler = ConversationHandler(
    entry_points=[CommandHandler('done', done_reminders)],
    states={
        0: [MessageHandler(filters.TEXT & ~filters.COMMAND, done_reminders_2)]
    },
    fallbacks = [],
)


conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("login", login_username)],
        states={
            0: [MessageHandler(filters.TEXT & ~filters.COMMAND, login_password)],
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_credentials)],
        },
        fallbacks=[],
    )


add_reminder_conv = ConversationHandler(
        entry_points=[CommandHandler("add", start_add_reminder)],
        states={
            0: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_title)],
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_text)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_date)],
        },
        fallbacks=[],
    )
