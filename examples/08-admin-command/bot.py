"""
Example 08 – Admin command

This bot demonstrates how to restrict certain commands to a list of
administrator user IDs.  The `/admin` command is only accessible to
authorised users defined in the `ADMIN_IDS` environment variable.  Other
users will receive a denial message.
"""

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN.")


def parse_admin_ids(raw: str) -> set[int]:
    """Parse ADMIN_IDS from a comma-separated environment variable."""
    admin_ids: set[int] = set()
    for item in raw.split(","):
        item = item.strip()
        if not item:
            continue
        try:
            admin_ids.add(int(item))
        except ValueError as exc:
            raise RuntimeError("ADMIN_IDS must be a comma-separated list of numeric Telegram user IDs.") from exc
    return admin_ids


ADMIN_IDS = parse_admin_ids(os.getenv("ADMIN_IDS", ""))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Use /admin for admin only actions.")


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorised to run this command.")
        return
    await update.message.reply_text("This is a restricted admin command.")


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin_command))
    application.run_polling()


if __name__ == "__main__":
    main()