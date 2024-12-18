from telegram import Update
from telegram.ext import ContextTypes
from bot.state_storage import BotStateStorage

state_storage = BotStateStorage()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if state_storage.get_state(update.message.from_user.id) is None:
        return await update.message.reply_text("Salom! shaxsiy accountingizga kirish uchun /login buyrug'idan foydalaning")
    return await update.message.reply_text(f"Salom! {update.message.from_user.first_name} xush kelibsiz")
