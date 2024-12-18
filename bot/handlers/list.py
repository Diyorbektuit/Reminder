from telegram import Update
from telegram.ext import ContextTypes
from reminder.models import Reminder
from bot.state_storage import BotStateStorage
from bot.functions import get_reminders

state_storage = BotStateStorage()

async def list_reminders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = state_storage.get_state(user_id=update.message.from_user.id)
    if state is None:
        return await update.message.reply_text("Siz hali tizimga kirmaganiz iltimos tizimga kiring /login")
    user_id = update.message.from_user.id
    response = await get_reminders(user_id)
    await update.message.reply_text(response)
