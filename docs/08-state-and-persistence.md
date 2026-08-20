# 08 – State and Persistence

## What you will build

In this chapter you will add **stateful behaviour** to your bot.  You will learn how to hold conversational context across multiple messages using the **ConversationHandler** and how to store user data across bot restarts using built‑in **persistence** backends.  You will build two examples: a simple in‑memory conversation and a bot that remembers user preferences using local file persistence.

## Why this concept exists

Most real bots need to remember things: which step of a conversation the user is in, or preferences like language or subscription status.  Without state, each message is independent and your bot cannot provide a coherent experience.  For development you can store state in memory, but for production you should persist it so that data is not lost when the bot restarts or the process crashes.  For storage trade-offs, see the [Storage / Persistence Comparison Matrix](comparisons.md#storage--persistence-comparison-matrix).

## Prerequisites

* Complete Stage 7 (Keyboards and callbacks).
* Knowledge of command and callback handlers.

## Code/files involved

* `examples/06-simple-state/bot.py` – demonstrates a two‑step conversation using `ConversationHandler`.
* `examples/07-persistence/bot.py` – demonstrates saving and loading data using PTB’s `PicklePersistence` (file‑based) or `DictPersistence`.

## Building a simple conversation

1. **Create the folder**:
   ```bash
   mkdir -p examples/06-simple-state
   cd examples/06-simple-state
   ```
2. **Write `bot.py`** for a multi‑step conversation:
   ```python
   import os
   from dotenv import load_dotenv
   from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
   from telegram.ext import (
       Application,
       CommandHandler,
       ConversationHandler,
       MessageHandler,
       ContextTypes,
       filters,
   )

   load_dotenv()
   TOKEN = os.getenv("BOT_TOKEN")

   ASK_NAME, ASK_AGE = range(2)

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       await update.message.reply_text("Hi! What is your name?")
       return ASK_NAME

   async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       context.user_data["name"] = update.message.text
       await update.message.reply_text(
           f"Nice to meet you, {update.message.text}! How old are you?",
           reply_markup=ReplyKeyboardMarkup([
               ["Under 18", "18–30", "30+"]
           ], one_time_keyboard=True, resize_keyboard=True),
       )
       return ASK_AGE

   async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       age_group = update.message.text
       name = context.user_data.get("name", "there")
       await update.message.reply_text(
           f"Thank you {name}! You selected {age_group}.", reply_markup=ReplyKeyboardRemove()
       )
       return ConversationHandler.END

   async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       await update.message.reply_text(
           "Conversation cancelled.", reply_markup=ReplyKeyboardRemove()
       )
       return ConversationHandler.END

   def main() -> None:
       application = Application.builder().token(TOKEN).build()
       conv_handler = ConversationHandler(
           entry_points=[CommandHandler("start", start)],
           states={
               ASK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
               ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
           },
           fallbacks=[CommandHandler("cancel", cancel)],
       )
       application.add_handler(conv_handler)
       application.run_polling()

   if __name__ == "__main__":
       main()
   ```
3. **Run the bot** and talk through the conversation.  Try sending `/cancel` to abort.

## Adding persistence

In the previous example, `context.user_data` is stored in memory and is lost when the bot restarts.  PTB provides persistence classes that save and restore user data, chat data, and conversation states.

1. **Create the folder**:
   ```bash
   mkdir -p examples/07-persistence
   cd examples/07-persistence
   ```
2. **Write `bot.py`** using `PicklePersistence`:
   ```python
   import os
   from dotenv import load_dotenv
   from telegram import Update
   from telegram.ext import (
       Application,
       CommandHandler,
       ConversationHandler,
       MessageHandler,
       ContextTypes,
       PicklePersistence,
       filters,
   )

   load_dotenv()
   TOKEN = os.getenv("BOT_TOKEN")

   ASK_FAVORITE = 0

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       user_id = update.effective_user.id
       favorite = context.user_data.get("favorite_color")
       if favorite:
           await update.message.reply_text(
               f"Your favorite color is still {favorite}. Send a new one or /cancel."
           )
       else:
           await update.message.reply_text("What is your favorite color?")
       return ASK_FAVORITE

   async def set_favorite(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       context.user_data["favorite_color"] = update.message.text
       await update.message.reply_text(
           f"Got it! I will remember that your favorite color is {update.message.text}."
       )
       return ConversationHandler.END

   async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
       await update.message.reply_text("Okay, nothing saved.")
       return ConversationHandler.END

   def main() -> None:
       persistence = PicklePersistence(filepath="bot_data.pkl")
       application = Application.builder().token(TOKEN).persistence(persistence).build()
       conv_handler = ConversationHandler(
           entry_points=[CommandHandler("start", start)],
           states={
               ASK_FAVORITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_favorite)],
           },
           fallbacks=[CommandHandler("cancel", cancel)],
       )
       application.add_handler(conv_handler)
       application.run_polling()

   if __name__ == "__main__":
       main()
   ```
3. **Run the bot**, set your favourite colour, then stop and restart it.  The bot should remember your choice on the next `/start`.

## Verify it

* The simple conversation collects your name and age group and ends after two messages.
* Cancelling the conversation returns to a neutral state.
* With persistence, the bot remembers your favourite colour across restarts.

## What just happened

You used `ConversationHandler` to manage multi‑step interactions and `PicklePersistence` to persist user data between sessions.  PTB also supports `DictPersistence` (in‑memory only) and `SQLitePersistence` (requires installing `aiosqlite`), which you can explore in the future.

## Common mistakes

- **Not returning the next state** from handler functions.  Each handler must return an integer key corresponding to the next state or `ConversationHandler.END`.
- **Forgetting to assign persistence** when building the application.  Without `persistence=...` the user data will not be saved.
- **Storing large or sensitive objects** in `PicklePersistence`.  Use caution with pickled data and consider database storage for production.

## Troubleshooting links

If your bot does not remember data:

- Ensure the `PicklePersistence` file path is writable by the process.
- Check that you passed the persistence instance to `Application.builder().persistence(...)`.
- Remember to use unique keys for different data items (e.g. `favorite_color`).

## Where it fits in the lifecycle

State and persistence appear after the **app logic** in the lifecycle.  They allow your bot to remember information for the next update or across restarts.

## Next step

In [09 – Security Baseline](09-security-baseline.md) you will learn how to protect your bot token, restrict access to administrative commands, and handle sensitive data responsibly.
