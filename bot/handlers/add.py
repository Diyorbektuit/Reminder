from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime
from bot.functions import add_reminder

TITLE, TEXT, DATE = range(3)

async def start_add_reminder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eslatma sarlavhasini kiriting.")
    return TITLE

async def get_title(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['title'] = update.message.text
    await update.message.reply_text("Eslatma matnini kiriting.")
    return TEXT

async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['text'] = update.message.text
    await update.message.reply_text("Eslatma vaqtini kiriting (YYYY-MM-DD HH:MM formatida).")
    return DATE

async def get_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_id = update.message.from_user.id
        date_str = update.message.text
        reminder_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        await add_reminder(
            telegram_id=str(user_id),
            title=context.user_data['title'],
            text=context.user_data['text'],
            date=reminder_date
        )
        await update.message.reply_text(f"Eslatma saqlandi: {context.user_data['title']} {reminder_date}")
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("Xato! Vaqt formatini to'g'ri kiriting (YYYY-MM-DD HH:MM).")
        return DATE
