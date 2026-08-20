"""
Handlers for the structured handlers example.

Define bot commands and callbacks here to keep the main application file clean.
"""

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a menu with buttons on /start."""
    await update.message.reply_text(
        "Welcome! Choose an option:", reply_markup=main_menu()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Display help information."""
    text = (
        "Commands:\n"
        "/start – show main menu\n"
        "/help – show this help message"
    )
    await update.message.reply_text(text)


async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle callback queries from inline keyboard buttons."""
    query = update.callback_query
    await query.answer()
    data = query.data
    if data == "HELLO":
        await query.edit_message_text("Hello again from structured handlers!")
    elif data == "HELP":
        await query.edit_message_text(
            "Use /help to see the command list."
        )


def register_handlers(application: Application) -> None:
    """Register handlers on the given Application."""
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(handle_button))