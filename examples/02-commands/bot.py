"""
Example 02 – Multiple commands and echo

This bot extends the simple echo bot with additional commands:
  * /start – greet the user
  * /help – show a list of commands
  * /caps <text> – convert text to uppercase

Non‑command messages are still echoed.  Use this example to practise
registering multiple handlers and using context arguments.
"""

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Use /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "Available commands:\n"
        "/start – greet the user\n"
        "/help – show this help message\n"
        "/caps <text> – convert text to uppercase"
    )
    await update.message.reply_text(text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        text_caps = ' '.join(context.args).upper()
        await update.message.reply_text(text_caps)
    else:
        await update.message.reply_text("Usage: /caps <text>")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("caps", caps))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()

if __name__ == "__main__":
    main()