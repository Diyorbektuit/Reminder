from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from bot.functions import authenticate_user, telegram_user_create, delete_telegram_user
from bot.state_storage import BotStateStorage

state_storage = BotStateStorage()

USERNAME, PASSWORD = range(2)


async def login_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Iltimos, usernameingizni kiriting.")
    return USERNAME


async def login_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text
    context.user_data['username'] = username
    await update.message.reply_text("Endi parolingizni kiriting.")
    return PASSWORD


async def check_credentials(update: Update, context: ContextTypes.DEFAULT_TYPE):
    password = update.message.text
    username = context.user_data.get('username')
    tg_username = update.message.from_user.username
    user = await authenticate_user(username=username, password=password)

    if user is not None:
        state_storage.set_state(user_id=update.message.from_user.id, state="logged_in")
        await telegram_user_create(
            user=user, telegram_id=update.message.from_user.id, username=tg_username
        )
        await update.message.reply_text("Siz muvaffaqiyatli kirgansiz!")
        return ConversationHandler.END
    else:
        await update.message.reply_text("Username yoki parol noto'g'ri.")
        return ConversationHandler.END

async def logout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    state_storage.clear_state(user_id)
    is_true = await delete_telegram_user(user_id)
    await update.message.reply_text("Siz tizimdan chiqdingiz.")


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Login jarayoni bekor qilindi.")
    return ConversationHandler.END