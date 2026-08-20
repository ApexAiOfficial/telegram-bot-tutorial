# 03 – Bot API Fundamentals

## What you will build

In this chapter you will write your first lines of bot code.  You will create a minimal echo bot that listens for updates via **long polling** and replies with the same text.  You will also learn about the structure of updates and messages as defined by the Telegram Bot API.

## Why this concept exists

The Telegram Bot API defines how your bot communicates with Telegram’s servers.  Understanding updates, messages, and the difference between long polling and webhooks is crucial for writing responsive bots.  Long polling is ideal for local development because it requires no public URL; webhooks come later for deployment.

## Prerequisites

* Complete Stage 2 (BotFather and token safety).  Ensure your `.env` file contains a valid `BOT_TOKEN`.
* Your virtual environment is active and the root `requirements.txt` has been installed (PTB v22.8 with the webhook extra).

## Code/files involved

* `examples/01-echo-bot/bot.py` – the Python script you will create in this stage.
* `.env` – contains your `BOT_TOKEN`.

## Run it

1. **Navigate to the example folder**:
   ```bash
   cd examples/01-echo-bot
   ```
2. **Create `bot.py`** with the following content:
   ```python
   import os
   from dotenv import load_dotenv
   from telegram import Update
   from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

   # Load environment variables
   load_dotenv()
   TOKEN = os.getenv("BOT_TOKEN")

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       """Send a welcome message when the /start command is issued."""
       await update.message.reply_text("Hello! I will echo your messages. Send me something.")

   async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       """Echo the user message."""
       if update.message and update.message.text:
           await update.message.reply_text(update.message.text)

   def main() -> None:
       # Build the application
       application = Application.builder().token(TOKEN).build()
       # Register handlers
       application.add_handler(CommandHandler("start", start))
       application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
       # Start the bot using long polling
       application.run_polling()

   if __name__ == "__main__":
       main()
   ```
3. **Run the bot**:
   ```bash
   python bot.py
   ```
4. **Talk to your bot.**  Open the Telegram app, search for your bot and send `/start`.  The bot should reply with a welcome message.  Send any other message and it will echo back the same text.

## Verify it

* The bot process prints “`Bot is polling`” (from the underlying library) and continues running.
* Your bot responds to `/start` and echoes your messages.

## What just happened

You wrote a minimal bot using `python‑telegram‑bot`.  You imported `Application` to build the bot, registered a command handler and a message handler, and started long polling.  Long polling repeatedly requests updates from Telegram.  The `telegram.ext` API dispatches incoming updates to the appropriate handler based on filters.

## Common mistakes

- **Forgetting to load the `.env` file.** Without `load_dotenv()` the token may be `None`, causing authentication errors.
- **Using `print(update.message.text)` instead of replying.** Your bot must use `reply_text` to send messages via the Bot API.
- **Not excluding commands from the echo handler.** If you don’t use `~filters.COMMAND`, the echo handler will also respond to `/start`, resulting in duplicate replies.

## Troubleshooting links

If the bot does not respond:

- Check for `Unauthorized` errors – your `BOT_TOKEN` may be invalid (see the troubleshooting entry on invalid tokens).
- Ensure your internet connection allows outgoing HTTPS traffic.
- Verify that your virtual environment is activated and `python-telegram-bot` is installed.

## Where it fits in the lifecycle

This is the first code‑running stage in the lifecycle.  It exercises the left side of the mental model: **User → Telegram update → bot backend → handler → app logic → Bot API call → Telegram → user**.

## Next step

Proceed to [04 – Backend Reality](04-backend-reality.md) to learn about the process lifecycle, concurrency and how your bot code runs, or jump to [06 – Commands and Handlers](06-commands-and-handlers.md) to extend your bot with more commands.