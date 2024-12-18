from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from bot.state_storage import BotStateStorage
from bot.functions import delete_reminder

state_storage = BotStateStorage()

REMINDER_ID = 0

async def delete_reminder_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    state = state_storage.get_state(user_id=update.message.from_user.id)
    if state is None:
        return await update.message.reply_text("Siz hali tizimga kirmaganiz iltimos tizimga kiring /login")
    await update.message.reply_text("o'chirmoqchi bo'lgan eslatmangizni idsini kiriting")
    return REMINDER_ID


async def delete_reminder_handler_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reminder_id = update.message.text
    user_id = update.message.from_user.id
    result = await delete_reminder(reminder_id=reminder_id, user_id=str(user_id))
    if result:
        await update.message.reply_text("eslatma muvaffaqiyatli o'chirildi")
        return ConversationHandler.END
    await update.message.reply_text("elsatma idsi xato")
    return ConversationHandler.END


