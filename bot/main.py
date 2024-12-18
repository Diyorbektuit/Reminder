import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.develop')
django.setup()

from telegram.ext import Application, CommandHandler
import environ
from handlers import add_reminder_conv, conversation_handler, start, \
    list_reminders, logout, cancel, reminder_done_handler

env = environ.Env()
env.read_env(".env")

BOT_TOKEN = env.str("BOT_TOKEN")
application = Application.builder().token(BOT_TOKEN).build()

def main():
    print("start")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", list_reminders))

    application.add_handler(CommandHandler("logout", logout))
    application.add_handler(CommandHandler("cancel", cancel))

    application.add_handler(add_reminder_conv)
    application.add_handler(conversation_handler)
    application.add_handler(reminder_done_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
