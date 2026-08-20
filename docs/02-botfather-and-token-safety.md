# 02 – BotFather and Token Safety

## What you will build

In this stage you will register your bot with Telegram via BotFather and learn how to handle the bot token securely.  The result will be a `.env` file containing your token and a `.gitignore` that prevents secrets from being committed.

## Why this concept exists

Every Telegram bot is identified by a token issued by BotFather.  Anyone who obtains this token can control your bot, so leaking it is equivalent to handing over your bot to a stranger.  Proper token management is therefore one of the first security practices to adopt.

## Prerequisites

* Complete Stage 1 to set up your environment and install dependencies.
* A Telegram account with access to the BotFather bot.

## Code/files involved

* `.env` – stores your bot token and other secrets; excluded from version control.
* `.env.example` – provides a template; safe to commit.
* `.gitignore` – already configured to ignore `.env`.

## Run it

1. **Start BotFather.**  Open Telegram and search for `@BotFather`.  Start a conversation and send `/start` to see the list of commands.
2. **Create a new bot.**  Send `/newbot` and follow the prompts:
   * Choose a **display name** – this can include spaces.
   * Choose a **username** – must end in `bot` and be unique.  Telegram will confirm availability.
3. **Copy the token.**  After the bot is created, BotFather displays a bot token.  Copy it into `.env` without pasting it into any source file.  This repository intentionally avoids showing realistic token-shaped examples.
4. **Store the token in `.env`.**  In your project directory:
   ```bash
   echo "BOT_TOKEN=<paste-your-token-here>" >> .env
   ```
   Make sure there are no extra spaces.  If you have admin commands later, you can also add `ADMIN_IDS` to this file.
5. **Rotate the token if leaked.**  If you ever expose your token (e.g. committing it to GitHub), go back to BotFather and use `/revoke` to generate a new one.  Update your `.env` accordingly.

## Verify it

* Your `.env` file contains a line beginning with `BOT_TOKEN=` followed by a token.
* Running `print(os.getenv('BOT_TOKEN'))` in a Python REPL within the venv returns your token.
* `.env` is not listed when running `git status` because `.gitignore` excludes it.

## What just happened

You created a Telegram bot with BotFather and learned how to store its token securely.  You also learned how to rotate a token if it leaks and how `.env` and `.gitignore` work together to keep secrets out of version control.

## Common mistakes

- **Committing the token.**  Always double‑check your commits before pushing.  Use `git status` and inspect staged files.
- **Pasting the token directly into code.**  Never hardcode secrets in Python files.  Use environment variables instead.
- **Using the wrong bot.**  If you manage multiple bots, ensure you copied the correct token.

## Troubleshooting links

Refer to the [troubleshooting guide](troubleshooting.md) if you encounter:

- `Unauthorized` errors – your token may be invalid or expired.
- Bot not appearing in search – the username may not end in `bot` or may be pending Telegram’s propagation.

## Where it fits in the lifecycle

This stage occurs before writing bot code.  It completes the foundational setup by linking a Bot API identity (your token) to your local environment.

## Next step

Proceed to [03 – Bot API Fundamentals](03-bot-api-fundamentals.md) to learn how updates work and to prepare for your first bot code.