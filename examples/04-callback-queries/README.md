# 04 – Callback Queries

This example expands on the inline keyboard by demonstrating how to handle **callback queries**.  When a user presses a button, Telegram sends a callback query to your bot.  You must acknowledge it with `answer()` to stop the loading spinner, then update the message or send a new one.

## Files

* `bot.py` – sends an inline keyboard on `/start` and handles button presses.

## Running the example

1. Make sure you have a `.env` file with `BOT_TOKEN` set.
2. Run the bot:
   ```bash
   python bot.py
   ```
3. Send `/start` to your bot and press a button.  The bot will edit the message to say hello or show a help message.

## What changed since the previous example

* Added `CallbackQueryHandler` to respond to button presses.
* Added a `button()` function that acknowledges the callback and edits the message.

## Common mistakes

- Forgetting to call `await query.answer()`.  Without acknowledging, the user’s Telegram client shows a continuous loading spinner.
- Forgetting to register the `CallbackQueryHandler` with the application.
