# 07 – Persistence

In this example you add persistence to your bot so that it remembers data across restarts.  The bot asks for the user’s favourite colour and stores it using `PicklePersistence`.  When restarted, the bot recalls the favourite colour.

## Files

* `bot.py` – bot script that uses `PicklePersistence` to save user data.
* `bot_data.pkl` – created at runtime to store user data; not committed to version control.

## Running the example

1. Ensure your `.env` file contains `BOT_TOKEN`.
2. Run the bot:
   ```bash
   python bot.py
   ```
3. Send `/start` to your bot.  If this is the first run, the bot asks for your favourite colour.  Provide a colour.  Stop the bot (Ctrl+C) and run it again.  Send `/start` again.  It should remember the colour.

## What changed since the previous example

* Added `PicklePersistence` to save `context.user_data` to disk.
* Stored user input under the key `favorite_color` in the user data dictionary.
* The bot checks existing user data before asking for input again.

## Common mistakes

- Forgetting to pass the persistence instance into `Application.builder().persistence(...)` – without it, nothing is saved.
- Not ignoring the persistence file in `.gitignore`.  Do not commit `bot_data.pkl` to your repository.
