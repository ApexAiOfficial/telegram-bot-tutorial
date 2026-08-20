# 01 – Absolute Zero Setup

## What you will build

In this stage you will prepare your development environment from scratch.  You will install Python 3.13, create a project folder with a virtual environment, install the required packages, configure a `.env` file and obtain a bot token from BotFather.  At the end of this stage you will be ready to run your first bot.

## Why this concept exists

Many beginners are derailed before they ever write a line of bot code because their environment isn’t properly configured.  A clean, isolated setup prevents version conflicts and keeps secrets out of your source code.  Starting with a `.env` and `.gitignore` also instils good security habits from day one.

## Prerequisites

* An internet connection to download Python and `python‑telegram‑bot`.
* A Telegram account to create a bot via BotFather.

## Code/files involved

* `requirements.txt` – lists Python dependencies.
* `.env.example` – template for environment variables.
* `.gitignore` – prevents committing secrets and generated files.
* No Python code yet; this stage is pure setup.

## Run it

1. **Install Python 3.13.**  Download Python from [python.org](https://www.python.org/downloads/).  Verify installation:
   ```bash
   python3 --version
   ```
   You should see a supported Python 3 version. For this tutorial, Python 3.13 remains a conservative choice. `python‑telegram‑bot` v22.8 requires Python 3.10+ and its v22.8 changelog records testing on Python 3.14; verify the current project requirements before choosing a newer interpreter.
2. **Create a project directory**:
   ```bash
   mkdir telegram-bot-tutorial
   cd telegram-bot-tutorial
   ```
3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   You should now see `(venv)` at the start of your shell prompt.
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Open `.env` in a text editor and set `BOT_TOKEN` to the token you will generate in the next step.  Optionally set `ADMIN_IDS` to your own Telegram user ID.
6. **Create your bot using BotFather**:
   * Open Telegram and start a chat with [@BotFather](https://t.me/BotFather).
   * Send `/start` and follow the prompts.
   * Use `/newbot` to create a new bot.  Provide a name and a username.
   * BotFather will respond with a token.  **Paste this token into your `.env` file**.  Never share it publicly.
   For more details, see [02 – BotFather and Token Safety](02-botfather-and-token-safety.md).

## Verify it

* Running `python3 --version` outputs `3.13.x`.
* `pip install -r requirements.txt` completes without errors.
* Your `.env` file contains a valid `BOT_TOKEN`.
* The project directory contains `.env`, `.env.example`, `.gitignore`, `requirements.txt` and this `docs/` folder.

## What just happened

You set up a clean Python environment, installed the dependencies and obtained a Telegram bot token.  You also learned the importance of keeping secrets out of source control.  These steps lay the foundation for all subsequent stages.

## Common mistakes

- **Using the system Python.** Always use a virtual environment to avoid clashing with other projects.
- **Forgetting to activate the venv.** If you see module import errors, double‑check that `(venv)` appears in your shell prompt.
- **Committing `.env`.** Never commit your `.env` file or real tokens.  The `.gitignore` in the repo excludes it.
- **Mixing Python versions.** Installing packages with one Python and running with another leads to mysterious errors.

## Troubleshooting links

Refer to the [troubleshooting guide](troubleshooting.md) if you encounter:

- `python3: command not found` – Python is not installed or not in your PATH.
- `ModuleNotFoundError: No module named 'telegram'` – dependencies were not installed or the venv is not active.
- Invalid token errors – see the BotFather section and the troubleshooting entry on invalid tokens.

## Where it fits in the lifecycle

This stage sits before any bot code runs.  It prepares your environment so that the subsequent stages can focus solely on bot logic.

## Next step

Proceed to [02 – BotFather and Token Safety](02-botfather-and-token-safety.md) to learn how to manage your bot token securely and configure your `.env` file.