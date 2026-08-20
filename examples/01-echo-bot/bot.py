"""
Example 01 – Echo bot

This script implements a minimal echo bot using python‑telegram‑bot.  It listens for the
/start command and echoes any subsequent text messages.  Use this example to verify
your environment and token configuration.  Run it with:

    python bot.py

Ensure you have installed dependencies (`pip install -r requirements.txt`) and set
your `BOT_TOKEN` in a `.env` file before running.
"""

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Load environment variables from .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text("Hello! I will echo your messages. Send me something.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message back to them."""
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

def main() -> None:
    """Start the bot using long polling."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == "__main__":
    main()