# 02 – Commands

This example demonstrates how to register multiple command handlers and a message handler while still echoing non‑command messages.  New commands include `/help` and `/caps` (convert text to uppercase).

## Files

* `bot.py` – the bot implementation with command handlers and an echo handler.

## Running the example

1. Install dependencies if you haven’t already:
   ```bash
   pip install python-telegram-bot==22.8 python-dotenv
   ```
2. Copy and edit the `.env` file:
   ```bash
   cp ../../.env.example .env
   # edit .env to set BOT_TOKEN=your token
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```
4. In Telegram, send `/help` to see a list of commands.  Test `/caps hello world` and verify that it returns `HELLO WORLD`.  Any other text message should be echoed.

## What changed since the previous example

* Added `/help` command using `CommandHandler("help", ...)`.
* Added `/caps` command that demonstrates how to access command arguments via `context.args`.
* Reordered handlers so that command handlers run before the echo handler.

## Common mistakes

- Registering the echo handler before command handlers; commands might get intercepted by the echo handler.  Always register command handlers first.
- Forgetting to join `context.args` into a string when using them.
