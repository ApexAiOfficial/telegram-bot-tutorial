# 06 – Commands and Handlers

## What you will build

You will extend your bot to support multiple **commands** beyond `/start`.  Commands let users invoke specific actions by sending messages beginning with a slash (`/`).  You will also learn about **message handlers** and **filters** so your bot only reacts to certain types of updates.  At the end of this chapter you will have a bot that responds to `/start`, `/help`, and `/caps`, and still echoes other text messages.

## Why this concept exists

Handlers are the core abstraction in **python‑telegram‑bot**.  A handler tells the dispatcher “when you see an update matching this filter, call this function”.  Commands provide a simple user interface for features and are automatically recognized by Telegram clients.  Filters keep your handlers focused and prevent unintended triggers.

## Prerequisites

* Complete Stage 5 (Polling vs Webhooks) and understand how updates reach your bot.
* Your `.env` contains a valid `BOT_TOKEN`.

## Code/files involved

* `examples/02-commands/bot.py` – new script implementing additional commands.
* `.env` – still holds your bot token.

## Implement commands and handlers

1. **Create the example folder** if it doesn’t exist:
   ```bash
   mkdir -p examples/02-commands
   cd examples/02-commands
   ```
2. **Write `bot.py`** with the following content:
   ```python
   import os
   from dotenv import load_dotenv
   from telegram import Update
   from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

   load_dotenv()
   TOKEN = os.getenv("BOT_TOKEN")

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
       # Join all arguments passed to the command and convert to uppercase
       if context.args:
           text_caps = ' '.join(context.args).upper()
           await update.message.reply_text(text_caps)
       else:
           await update.message.reply_text("Usage: /caps <text>")

   async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
       # Echo any non‑command text
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
   ```
3. **Run the bot**:
   ```bash
   python bot.py
   ```
4. **Talk to your bot**: Send `/help` and `/caps hello world` to see the responses.  Non‑command messages will still be echoed.

## Verify it

* The bot responds correctly to `/start`, `/help`, and `/caps`.
* The `caps` command returns uppercase text for any arguments provided.
* Messages not starting with `/` are echoed.

## What just happened

You created new **command handlers** to respond to specific slash commands.  You also used a **message handler** with a filter to match only text that is not a command.  The `context.args` list contains arguments passed to the command.  This pattern scales to many commands while keeping your handlers clear.

## Common mistakes

- **Not using filters**: Without `~filters.COMMAND`, the echo handler will reply to commands as well, producing confusing duplicate messages.
- **Forgetting to join arguments**: `context.args` is a list; use `' '.join(context.args)` to reconstruct the full text.
- **Registering handlers in the wrong order**: Command handlers should come before more generic handlers.  The dispatcher checks handlers in the order they were added.

## Troubleshooting links

If commands do not trigger:

- Ensure your bot is added as administrator in group chats for commands starting with `/` to work.
- Verify that your Telegram client is not in **privacy mode** for group bots; commands may be hidden unless preceded by the bot’s username (e.g. `/help@YourBotName`).

## Where it fits in the lifecycle

This chapter focuses on the **handler** layer.  Commands are a special type of message that the dispatcher recognises and routes to your defined function.

## Next step

Continue to [07 – Keyboards and Callbacks](07-keyboards-and-callbacks.md) to learn how to add inline keyboards and handle user interactions beyond plain text.
