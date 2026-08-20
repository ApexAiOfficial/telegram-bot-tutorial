# Glossary

This glossary defines key terms used throughout the tutorial.  Refer to it whenever you encounter unfamiliar terminology.

| Term | Definition |
|---|---|
| **Bot API** | The HTTPS API exposed by Telegram for bot developers.  Bots send and receive messages via this API. |
| **update** | A JSON object representing an event sent by Telegram to your bot.  It may contain messages, edited messages, callback queries, etc. |
| **message** | A particular type of update representing a text, photo, sticker, or other content sent by a user or channel. |
| **command** | A message beginning with a slash (`/`) that invokes a specific bot action (e.g. `/start`). |
| **handler** | A function that processes incoming updates.  In python‑telegram‑bot, handlers are registered on an `Application` and triggered by filters. |
| **filter** | A rule that determines which updates a handler should receive.  For example, `filters.TEXT & ~filters.COMMAND` matches text messages that are not commands. |
| **dispatcher** | The component within the `Application` that routes updates to the appropriate handlers. |
| **callback query** | A special type of update generated when a user presses an inline keyboard button.  It contains the button’s callback data. |
| **ConversationHandler** | A class in python‑telegram‑bot that manages multi‑step dialogues.  It maps user responses to states and transitions. |
| **persistence** | The ability to save and restore bot state across restarts.  PTB provides `DictPersistence`, `PicklePersistence`, and `SQLitePersistence`. |
| **long polling** | A method of retrieving updates where the bot repeatedly calls `getUpdates` and waits for new messages.  Suitable for local development. |
| **webhook** | A method of receiving updates via an HTTP POST from Telegram to your server. Webhooks and long polling are alternative Telegram update-delivery mechanisms; this tutorial uses webhooks as the canonical public web-service deployment path. |
| **webhook secret** | A token you can set when configuring the webhook.  Telegram includes this token in the `X‑Telegram‑Bot‑Api‑Secret-Token` header of webhook requests for verification. |
| **BotFather** | Telegram’s official bot for creating and managing other bots.  You obtain your bot token from BotFather. |
| **Bot token** | A string provided by BotFather that uniquely identifies and authenticates your bot.  Keep it secret. |
| **admin ID** | The Telegram user ID of an administrator allowed to run privileged commands. |
| **render** | A cloud hosting provider used in this tutorial for deployment.  Offers free and paid tiers. |
| **venv** | A Python virtual environment that isolates your project’s dependencies.  Created with `python -m venv .venv`. |

If you encounter other terms, consider adding them here to expand the glossary.
