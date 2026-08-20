"""
Example 09 – Logging and error handling

This example shows how to configure basic logging for your bot and how to
define an error handler.  Proper logging helps you debug issues in
production and avoid printing sensitive data.  The bot still implements
simple commands as before.
"""

import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Logging example running. Use /error to trigger an error.")


async def error_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # This command intentionally raises an exception to demonstrate error handling
    raise RuntimeError("This is a test error")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a generic message to the user."""
    logger.error(msg="Exception while handling an update", exc_info=context.error)
    if isinstance(update, Update) and update.effective_message:
        await update.effective_message.reply_text(
            "An unexpected error occurred. Please try again later."
        )


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("error", error_command))
    application.add_error_handler(error_handler)
    application.run_polling()


if __name__ == "__main__":
    main()