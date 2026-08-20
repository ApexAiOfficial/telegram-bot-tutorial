# 01 – Echo Bot

This example demonstrates the simplest possible Telegram bot.  It listens for the `/start` command and echoes any text messages back to the user.  Use this project to verify that your environment and token are configured correctly.

## Files

* `bot.py` – the bot source code.  See the docstring for details.
* `bot.py` – the bot source code.  Copy the repository-root `.env.example` into this folder or provide `BOT_TOKEN` via your shell environment.

## Running the example

1. Install dependencies (once per environment):
   ```bash
   pip install python-telegram-bot==22.8 python-dotenv
   ```
2. Copy the `.env.example` from the root of this repository and edit it:
   ```bash
   cp ../../.env.example .env
   # then edit .env and set BOT_TOKEN=<your token>
   ```
3. Run the bot:
   ```bash
   python bot.py
   ```
4. In Telegram, open your bot (created via BotFather), send `/start`, then send any text message.  The bot should reply with the same text.

## What changed since the previous stage

This is the first runnable example.  It introduces `CommandHandler` for `/start` and `MessageHandler` with a simple filter for text.  It also demonstrates loading environment variables from `.env` using `dotenv`.

## Common mistakes

- Not creating a `.env` file with your bot token.
- Forgetting to activate your virtual environment before running the bot.
- Leaving the echo handler too broad (e.g. not excluding commands).  This is corrected in later examples.
