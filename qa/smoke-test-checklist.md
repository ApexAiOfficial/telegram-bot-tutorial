# Smoke Test Checklist

This checklist verifies each example from a predictable working directory.  Unless a row says otherwise, run commands from the **repository root** after creating `.env` from `.env.example`.

## Common setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cp .env.example .env
# edit .env and set BOT_TOKEN=your token; set ADMIN_IDS for admin examples
```

## Example smoke tests

| Example | Working directory | Run command | Expected behaviour | Pass/Fail |
|---|---|---|---|---|
| **01-echo-bot** | repo root | `python examples/01-echo-bot/bot.py` | `/start` replies with greeting; any text is echoed. | |
| **02-commands** | repo root | `python examples/02-commands/bot.py` | `/start`, `/help`, and `/caps hello` return appropriate messages; other text is echoed. | |
| **03-inline-keyboard** | repo root | `python examples/03-inline-keyboard/bot.py` | `/start` shows two buttons; pressing them does not act yet. | |
| **04-callback-queries** | repo root | `python examples/04-callback-queries/bot.py` | `/start` shows buttons; pressing “Say hello” edits message to hello; pressing “Show help” edits message with help text. | |
| **05-structured-handlers** | `examples/05-structured-handlers` | `python main.py` | `/start` shows menu; buttons reply accordingly; `/help` shows help. | |
| **06-simple-state** | repo root | `python examples/06-simple-state/bot.py` | `/start` asks for name, then age group; replies with confirmation; `/cancel` aborts. | |
| **07-persistence** | repo root | `python examples/07-persistence/bot.py` | First run: `/start` asks for favourite colour and saves it. After restart: `/start` recalls the colour. | |
| **08-admin-command** | repo root | `python examples/08-admin-command/bot.py` | `/admin` only responds for user IDs in `ADMIN_IDS`; others see denial. | |
| **09-logging-errors** | repo root | `python examples/09-logging-errors/bot.py` | `/start` prints message; `/error` triggers error, logs stack trace, and replies with generic error message. | |
| **10-docker** | repo root | `docker build -f examples/10-docker/Dockerfile -t telegram-bot-example:latest .` then `docker run --env-file .env telegram-bot-example:latest` | Behaves like the echo bot; `/start` and text messages work. | |
| **11-webhook-deploy** | repo root | `WEBHOOK_URL=https://example.com/webhook WEBHOOK_SECRET=test_secret_123456 PORT=8443 python examples/11-webhook-deploy/bot.py` | Webhook server starts; after setting a real webhook on a real host, messages are delivered via webhook. | |
| **12-capstone** | repo root | `python examples/12-capstone/bot.py` | `/start` shows menu; `SHOW` displays stored colour or “not set”; `UPDATE` asks for a colour; reply is saved persistently; `/cancel` exits cleanly. | |

## Notes

- Telegram runtime tests require a real bot token. If no token is available, mark runtime status as **NOT RUN**.
- Do not commit `.env` files or persistence files such as `bot_data.pkl` or `capstone_data.pkl`.
- For webhook examples, set `WEBHOOK_URL`, `PORT`, and a non-empty `WEBHOOK_SECRET`, then verify webhook delivery on a real HTTPS host.
