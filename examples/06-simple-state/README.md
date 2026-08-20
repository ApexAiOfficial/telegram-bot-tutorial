# 06 – Simple State

This example introduces **conversation state** using a `ConversationHandler`.  The bot asks the user for their name, then for an age group, and then ends the conversation.  State is stored in memory and is lost when the bot restarts.

## Files

* `bot.py` – implements a two‑step conversation with `/start` and `/cancel` commands.

## Running the example

1. Ensure your `.env` file contains `BOT_TOKEN` and that dependencies are installed.
2. Run the bot:
   ```bash
   python bot.py
   ```
3. Send `/start` to begin the conversation.  Answer the questions.  Send `/cancel` to stop at any time.

## What changed since the previous examples

* Added `ConversationHandler` to manage multi‑step interactions.
* Introduced `context.user_data` to store user‑specific information (name) across steps.
* Used `ReplyKeyboardMarkup` to provide quick reply options for the age question.

## Common mistakes

- Returning the wrong state value from a handler.  Each handler must return the next state constant or `ConversationHandler.END`.
- Storing data in a global variable instead of `context.user_data`, which would mix data from different users.
- Not removing the reply keyboard with `ReplyKeyboardRemove()` at the end of the conversation.
