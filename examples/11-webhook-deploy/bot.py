"""Example 11 – authenticated webhook deployment."""

import logging
import os
import re
from urllib.parse import urlparse

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
PORT = int(os.getenv("PORT", "8443"))

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")
if not WEBHOOK_URL:
    raise RuntimeError("WEBHOOK_URL must be set when using the public webhook example.")
if not WEBHOOK_SECRET:
    raise RuntimeError("WEBHOOK_SECRET must be set for the public webhook example; refusing unauthenticated webhook startup.")
if not re.fullmatch(r"[A-Za-z0-9_-]{16,256}", WEBHOOK_SECRET):
    raise RuntimeError("WEBHOOK_SECRET must be 16-256 characters using only letters, digits, underscore, or hyphen.")

parsed = urlparse(WEBHOOK_URL)
if parsed.scheme != "https" or not parsed.netloc or not parsed.path or parsed.path == "/":
    raise RuntimeError("WEBHOOK_URL must be a public HTTPS URL with a non-root path, e.g. https://example.com/webhook")
WEBHOOK_PATH = parsed.path


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Webhook example running. Send me a message!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message and update.message.text:
        await update.message.reply_text(update.message.text)


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("echo", echo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=WEBHOOK_PATH.lstrip("/"),
        webhook_url=WEBHOOK_URL,
        secret_token=WEBHOOK_SECRET,
    )


if __name__ == "__main__":
    main()
