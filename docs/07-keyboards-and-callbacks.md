# 07 – Keyboards and Callbacks

## What you will build

In this chapter you will learn how to create **inline keyboards** and respond to **callback queries**.  Inline keyboards allow users to press buttons attached to messages instead of typing commands.  When a button is pressed, Telegram sends a callback query to your bot, which you must answer.  You will build a bot that presents a simple menu with buttons and reacts accordingly.

## Why this concept exists

Bots become more user‑friendly when they offer buttons for common actions.  Inline keyboards reduce user typing, avoid command typos, and enable conversational interfaces.  Handling callback queries properly ensures responsive and compliant behaviour (Telegram expects you to call `answerCallbackQuery`).

## Prerequisites

* Complete Stage 6 (Commands and handlers) and understand basic handler registration.
* Ensure your bot token is loaded from `.env`.

## Code/files involved

* `examples/03-inline-keyboard/bot.py` – sends a message with an inline keyboard.
* `examples/04-callback-queries/bot.py` – handles callback queries and acknowledges them.

## Sending an inline keyboard

1. **Create the example folder**:
   ```bash
   mkdir -p examples/03-inline-keyboard
   cd examples/03-inline-keyboard
   ```
2. **Write `bot.py`** to send a keyboard on `/start`:
   ```python
   import os
   from dotenv import load_dotenv
   from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
   from telegram.ext import Application, CommandHandler, ContextTypes

   load_dotenv()
   TOKEN = os.getenv("BOT_TOKEN")

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       keyboard = [
           [InlineKeyboardButton("Say hello", callback_data="HELLO")],
           [InlineKeyboardButton("Show help", callback_data="HELP")],
       ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       await update.message.reply_text(
           "Choose an action:", reply_markup=reply_markup
       )

   async def main() -> None:
       application = Application.builder().token(TOKEN).build()
       application.add_handler(CommandHandler("start", start))
       application.run_polling()

   if __name__ == "__main__":
       import asyncio
       asyncio.run(main())
   ```
3. **Run and test**:
   ```bash
   python bot.py
   ```
   In Telegram, send `/start`.  You should see two buttons.

This example does not handle the callback yet; pressing a button will show a loading spinner and then nothing.  That’s OK—we’ll handle callbacks next.

## Handling callback queries

Callback queries require two things: a handler that matches `CallbackQueryHandler` and a call to `answerCallbackQuery` to stop the client’s loading animation.  Let’s extend our bot in a separate example.

1. **Create a new folder**:
   ```bash
   mkdir -p examples/04-callback-queries
   cd examples/04-callback-queries
   ```
2. **Write `bot.py`** with callback handling:
   ```python
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

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       keyboard = [
           [InlineKeyboardButton("Say hello", callback_data="HELLO")],
           [InlineKeyboardButton("Show help", callback_data="HELP")],
       ]
       reply_markup = InlineKeyboardMarkup(keyboard)
       await update.message.reply_text("Choose an action:", reply_markup=reply_markup)

   async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       query = update.callback_query
       # Acknowledge the callback to stop the spinner
       await query.answer()
       data = query.data
       if data == "HELLO":
           await query.edit_message_text("👋 Hello there!")
       elif data == "HELP":
           await query.edit_message_text(
               "This is an example.  Use /start to see the keyboard again."
           )

   async def main() -> None:
       application = Application.builder().token(TOKEN).build()
       application.add_handler(CommandHandler("start", start))
       application.add_handler(CallbackQueryHandler(button))
       application.run_polling()

   if __name__ == "__main__":
       import asyncio
       asyncio.run(main())
   ```
3. **Run the bot** and press the buttons.  You should see the message update to reflect your choice.

## Verify it

* Pressing **Say hello** changes the message to “👋 Hello there!”.
* Pressing **Show help** shows a help message.
* The loading spinner disappears immediately after pressing.

## What just happened

You created an inline keyboard, attached it to a message, and handled the resulting callback queries.  You acknowledged the callback via `answer()` and edited the message based on `query.data`.  Inline keyboards make your bot more interactive and guide the user through options.

## Common mistakes

- **Not calling `answer()` on the callback query**.  Telegram will show a “loading” spinner until you acknowledge the query.
- **Using the wrong handler**.  Use `CallbackQueryHandler` for callback queries, not `MessageHandler`.
- **Forgetting to check `query.data`**.  The callback data string is your identifier; always validate it before acting.

## Troubleshooting links

If nothing happens when pressing a button:

- Check that you added the `CallbackQueryHandler` to your application.
- Ensure your code calls `await query.answer()`.
- Verify that the callback data matches your conditional checks.

## Where it fits in the lifecycle

This chapter extends the handler layer with **callback queries**.  Updates triggered by button presses still go through the same pipeline: **Update → Dispatcher → Handler → Response**.

## Next step

Proceed to [08 – State and Persistence](08-state-and-persistence.md) to learn how to keep track of user conversations and store data between sessions.
