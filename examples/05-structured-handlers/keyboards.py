"""
Keyboards for the structured handlers example.

Define inline keyboards in a separate module to keep handlers focused on
business logic.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu() -> InlineKeyboardMarkup:
    """Return the main menu inline keyboard."""
    keyboard = [
        [InlineKeyboardButton("Say hello", callback_data="HELLO")],
        [InlineKeyboardButton("Help", callback_data="HELP")],
    ]
    return InlineKeyboardMarkup(keyboard)