"""
Example 12 – Capstone bot

This example combines concepts from previous stages: commands, inline
keyboards, callback queries, conversation state, and persistence.  The bot
presents a menu with options to view and update the user’s favourite colour.
Favourite colours are stored persistently using `PicklePersistence`.
"""

import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
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


def main_menu() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Show favourite colour", callback_data="SHOW")],
        [InlineKeyboardButton("Update favourite colour", callback_data="UPDATE")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the capstone bot!", reply_markup=main_menu()
    )


async def show_favorite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    favorite = context.user_data.get("favorite_color")
    if favorite:
        await query.edit_message_text(
            f"Your favourite colour is {favorite}.", reply_markup=main_menu()
        )
    else:
        await query.edit_message_text(
            "You haven't set a favourite colour yet.", reply_markup=main_menu()
        )


async def ask_favorite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "What is your favourite colour? Send it as a normal message. Use /cancel to stop."
    )
    return ASK_FAVORITE


async def set_favorite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["favorite_color"] = update.message.text
    await update.message.reply_text(
        f"Favourite colour saved as {update.message.text}.", reply_markup=main_menu()
    )
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Cancelled.", reply_markup=main_menu())
    return ConversationHandler.END


def main() -> None:
    persistence = PicklePersistence(filepath="capstone_data.pkl")
    application = Application.builder().token(TOKEN).persistence(persistence).build()

    # Register the conversation handler before the generic callback handler so
    # UPDATE callbacks enter the conversation instead of being consumed elsewhere.
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(ask_favorite, pattern="^UPDATE$")],
        states={
            ASK_FAVORITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_favorite)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(conv_handler)
    application.add_handler(CallbackQueryHandler(show_favorite, pattern="^SHOW$"))
    application.run_polling()


if __name__ == "__main__":
    main()
