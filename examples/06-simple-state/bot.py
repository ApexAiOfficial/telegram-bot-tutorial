"""
Example 06 – Simple conversation with in‑memory state

This bot uses a ConversationHandler to ask the user for their name and age group.
Conversation state is stored in memory (context.user_data) and lost when the
process restarts.  Use this example to practise multi‑step dialogues.
"""

import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

ASK_NAME, ASK_AGE = range(2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Hi! What is your name?")
    return ASK_NAME


async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["name"] = update.message.text
    await update.message.reply_text(
        f"Nice to meet you, {update.message.text}! How old are you?",
        reply_markup=ReplyKeyboardMarkup([
            ["Under 18", "18–30", "30+"]
        ], one_time_keyboard=True, resize_keyboard=True),
    )
    return ASK_AGE


async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    age_group = update.message.text
    name = context.user_data.get("name", "there")
    await update.message.reply_text(
        f"Thank you {name}! You selected {age_group}.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Conversation cancelled.", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
            ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()