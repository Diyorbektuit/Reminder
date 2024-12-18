from telegram import Update
from telegram.ext import ContextTypes
from bot.state_storage import BotStateStorage
from bot.functions import done_reminder

state_storage = BotStateStorage()

REMINDER_ID = range(1)


async def done_reminders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = state_storage.get_state(user_id=update.message.from_user.id)
    if state is None:
        return await update.message.reply_text("Siz hali tizimga kirmaganiz iltimos tizimga kiring /login")
    await update.message.reply_text("bajarilgan qilmoqchi bo'lgan eslatmangizni idsini kiriting")
    return REMINDER_ID


async def done_reminders_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reminder_id = update.message.text
    result = await done_reminder(reminder_id=reminder_id)
    if result:
        return await update.message.reply_text("eslatma muvaffaqiyatli bajarilgan qilindi")
    return await update.message.reply_text("elsatma idsi xato")


