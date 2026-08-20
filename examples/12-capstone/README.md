# 12 – Capstone

This capstone example combines several features learned throughout the tutorial: commands, inline keyboards, callback queries, conversation state, and persistence.  The bot presents a menu that allows the user to view or update their favourite colour.  Favourite colours are stored using `PicklePersistence` so they persist across bot restarts.

## Files

* `bot.py` – main script implementing the capstone bot.
* `capstone_data.pkl` – generated at runtime to store user data persistently; ignored by version control.

## Running the example

1. Ensure your `.env` file includes `BOT_TOKEN`.
2. Install dependencies if necessary.
3. Run the bot:
   ```bash
   python bot.py
   ```
4. Send `/start` to display the main menu.
5. Select **Show favourite colour** to view your currently stored colour (if any).
6. Select **Update favourite colour** and send a new colour.  The bot saves the value and returns to the menu.
7. Restart the bot and verify that your colour is remembered.

## What changed since previous examples

* Combined inline keyboards and conversation handlers into a cohesive user flow.
* Added persistent storage using `PicklePersistence`.
* Allowed re‑entering the conversation handler when pressing **Update favourite colour** again.

## Common mistakes

- Forgetting to specify `allow_reentry=True` in the conversation handler.  Without it, callback queries may not trigger the conversation again.
- Registering a generic callback query handler before the conversation handler.  The `UPDATE` callback must enter the conversation first, while `SHOW` is handled by a separate pattern-specific callback handler.
