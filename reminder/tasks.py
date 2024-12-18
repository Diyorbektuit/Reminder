from celery import shared_task
from telegram import Bot
from .models import Reminder
from django.conf import settings
import asyncio

@shared_task
def send_reminder_task(reminder_id):
    bot = Bot(token=settings.BOT_TOKEN)
    reminder = Reminder.objects.filter(id=reminder_id)
    if not reminder.exists():
        return "reminder not found"
    try:
        reminder = reminder.first()
        user = reminder.user
        text = (f"SIZGA ESLATMA KELDI \n \n"
                f"{reminder.title} \n"
                f"{reminder.text}")
        if user.telegram is not None:
            asyncio.run(bot.send_message(chat_id=int(user.telegram.telegram_id), text=text))
            return "Message sent successfully"
        return "telegram user not found"
    except Exception as e:
        print(f"Error sending reminder {reminder.id}: {e}")
        return f"Error: {e}"
