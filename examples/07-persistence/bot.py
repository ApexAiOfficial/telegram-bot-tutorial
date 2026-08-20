"""
Example 07 – Persistence

This bot remembers a user’s favourite colour using python‑telegram‑bot’s
`PicklePersistence`.  Data is stored in a pickle file (bot_data.pkl) on disk.
After the bot restarts, the favourite colour is remembered.
"""

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    ContextTypes,
    PicklePersistence,
    filters,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

ASK_FAVORITE = 0


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    favorite = context.user_data.get("favorite_color")
    if favorite:
        await update.message.reply_text(
            f"Your favourite colour is still {favorite}. Send a new one or /cancel."
        )
    else:
        await update.message.reply_text("What is your favourite colour?")
    return ASK_FAVORITE


async def set_favorite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["favorite_color"] = update.message.text
    await update.message.reply_text(
        f"Got it! I will remember that your favourite colour is {update.message.text}."
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Okay, nothing saved.")
    return ConversationHandler.END


def main() -> None:
    persistence = PicklePersistence(filepath="bot_data.pkl")
    application = Application.builder().token(TOKEN).persistence(persistence).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            ASK_FAVORITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_favorite)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()