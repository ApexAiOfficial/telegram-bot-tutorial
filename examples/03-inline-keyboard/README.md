# 03 – Inline Keyboard

This example shows how to send an **inline keyboard** when a user sends `/start`.  The buttons themselves do not perform any action yet; they illustrate how to attach an inline keyboard to a message.  Callback handling is introduced in the next example.

## Files

* `bot.py` – sends an inline keyboard with two buttons.

## Running the example

1. Ensure you have installed dependencies and set your `BOT_TOKEN` in `.env`.
2. Run the bot:
   ```bash
   python bot.py
   ```
3. In Telegram, send `/start` to your bot.  You should see two buttons: **Say hello** and **Show help**.  When pressed, nothing happens yet; the callback data will be handled in the next example.

## What changed since the previous example

* Introduced `InlineKeyboardButton` and `InlineKeyboardMarkup` from `telegram`.
* The `/start` handler now attaches a keyboard instead of plain text.

## Common mistakes

- Forgetting to set `callback_data` for each button.  Without it, you cannot identify which button was pressed.
- Adding too many buttons on one row; use nested lists to create rows.
