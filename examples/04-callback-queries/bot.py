"""
Example 04 – Callback queries

This example builds upon the inline keyboard and shows how to handle
callback queries.  Pressing a button triggers a callback query that the bot
acknowledges using `answer()` and then edits the message accordingly.
"""

import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Say hello", callback_data="HELLO")],
        [InlineKeyboardButton("Show help", callback_data="HELP")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose an action:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "HELLO":
        await query.edit_message_text("👋 Hello there!")
    elif data == "HELP":
        await query.edit_message_text(
            "This is an example.  Use /start to see the keyboard again."
        )

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    main()