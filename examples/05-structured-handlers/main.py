"""
Example 05 – Structured handlers

This example refactors the bot code into separate modules for clarity.
Handlers are defined in `handlers.py` and keyboards in `keyboards.py`.  The
main entry point imports them and registers them on the application.
"""

import os
from dotenv import load_dotenv
from telegram.ext import Application

from handlers import register_handlers

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    register_handlers(application)
    application.run_polling()

if __name__ == "__main__":
    main()