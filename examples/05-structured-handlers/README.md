# 05 – Structured Handlers

As your bot grows, organising your code into modules improves readability and maintainability.  This example refactors the bot into separate files for handlers and keyboards.

## Files

| File | Purpose |
|---|---|
| `main.py` | Entry point that loads environment variables, builds the application, and registers handlers. |
| `handlers.py` | Contains the command handlers and callback query handler.  Also exposes a `register_handlers()` function. |
| `keyboards.py` | Defines the inline keyboard used in the main menu. |

## Running the example

1. Create a `.env` file with `BOT_TOKEN` (see previous examples).
2. Install dependencies if you haven’t already:
   ```bash
   pip install python-telegram-bot==22.8 python-dotenv
   ```
3. Run the bot:
   ```bash
   python main.py
   ```
4. Send `/start` to your bot.  You will see the main menu.  Press a button to see a response.

## What changed since the previous examples

* Moved handler logic into `handlers.py` and the keyboard definition into `keyboards.py`.
* Added a `register_handlers()` helper to decouple registration from the `Application` creation.
* Maintained the same functionality (start menu, hello/help) but improved structure.

## Common mistakes

- Forgetting to import `register_handlers` in `main.py`.
- Leaving multiple `Application` instances scattered across modules.  Only instantiate one application and register handlers on it.
