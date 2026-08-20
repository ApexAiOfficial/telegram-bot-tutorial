# 09 – Logging and Error Handling

This example introduces **logging** and a custom error handler.  Logging is essential for diagnosing problems in production without printing sensitive information.  The bot includes a command `/error` that intentionally raises an exception so you can see how the error handler works.

## Files

* `bot.py` – sets up logging, defines `/start` and `/error` commands, and registers a global error handler.

## Running the example

1. Ensure your `.env` contains `BOT_TOKEN`.
2. Run the bot:
   ```bash
   python bot.py
   ```
3. Send `/start` to see the welcome message.  Send `/error` to simulate an error.  The bot logs the exception and sends a generic message to the user.

## What changed since the previous examples

* Configured logging using `logging.basicConfig()` with a standard format.
* Added a `/error` command that raises an exception.
* Added an `error_handler` function registered via `application.add_error_handler()`.  It logs the error and replies to the user with a generic message.

## Common mistakes

- Logging sensitive information such as tokens or entire update payloads.  Limit log output to error details and messages.
- Forgetting to register the error handler; without it, unhandled exceptions stop the bot.
