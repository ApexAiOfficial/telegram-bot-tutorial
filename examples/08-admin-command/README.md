# 08 – Admin Command

In some bots you need to restrict certain commands to trusted users (administrators).  This example demonstrates how to load a list of admin user IDs from the `ADMIN_IDS` environment variable and check the caller before executing an admin command.

## Files

* `bot.py` – implements `/start` and `/admin`.  The `/admin` command is restricted.

## Running the example

1. Ensure your `.env` file includes:
   ```
   BOT_TOKEN=your_bot_token
   ADMIN_IDS=123456789,987654321
   ```
   Replace the numbers with your own Telegram user ID(s).
2. Install dependencies if needed.
3. Run the bot:
   ```bash
   python bot.py
   ```
4. From an authorised account, send `/admin` to receive the admin response.  From any other account, the bot will deny access.

## What changed since the previous examples

* Introduced environment variable `ADMIN_IDS` containing a comma‑separated list of authorised user IDs.
* Added a handler that checks `update.effective_user.id` against this set before proceeding.

## Common mistakes

- Not converting IDs to integers when loading from environment variables; user IDs are integers, not strings.
- Forgetting to include your own user ID in `ADMIN_IDS` when testing the command.
