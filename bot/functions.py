from datetime import datetime

from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from accounts.models import TelegramUser
from reminder.models import Reminder
from typing import Optional

@sync_to_async
def authenticate_user(username: str, password: str):
    """Foydalanuvchini tekshirish."""
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            return user
        return None
    except User.DoesNotExist:
        return None


@sync_to_async()
def telegram_user_create(user: User, telegram_id: int, username: Optional[str]):
    telegram_user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
    if not telegram_user:
        telegram_user = TelegramUser.objects.create(
            user=user,
            telegram_id=str(telegram_id),
            username=username
        )
    return telegram_user


def get_reminder_status(status: bool) -> str:
    if status:
        return "Bajarilgan"
    return "Bajarilmagan"


@sync_to_async()
def get_reminders(telegram_id):
    result = Reminder.objects.filter(user__telegram__telegram_id=telegram_id).order_by('date')

    if result.exists():
        response = "📝 **Sizning eslatmalaringiz:**\n\n"
        for count, reminder in enumerate(result, 1):
            response += (
                f"**{count}. {reminder.text}**\n"
                f"ID: {reminder.id} \n"
                f"📋 Status: `{get_reminder_status(reminder.status)}`\n"
                f"📅 Sana: `{reminder.date.strftime('%d-%m-%Y %H:%M')}`\n\n"
            )
        return response

    return "❌ Sizda hozircha eslatmalar yo'q."


@sync_to_async()
def delete_telegram_user(telegram_id):
    try:
        telegram_user = TelegramUser.objects.get(telegram_id=telegram_id)
        telegram_user.delete()
        return True
    except:
        return False


@sync_to_async()
def add_reminder(telegram_id: str, title: str, text: str, date: datetime):
    user = TelegramUser.objects.get(telegram_id=telegram_id).user
    new_reminder = Reminder.objects.create(
        user=user,
        title=title,
        text=text,
        date=date
    )
    return new_reminder


@sync_to_async()
def delete_reminder(reminder_id: int, user_id: str):
    user = TelegramUser.objects.get(telegram_id=user_id).user
    try:
        reminder = user.reminders.get(id=reminder_id)
        reminder.delete()
        return True
    except:
        return False


@sync_to_async()
def done_reminder(reminder_id: int, user_id: str):
    user = TelegramUser.objects.get(telegram_id=user_id).user
    try:
        reminder = user.reminders.get(id=reminder_id)
        reminder.status = True
        reminder.save()
        return True
    except:
        return False