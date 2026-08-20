# Troubleshooting

This page lists common problems you may encounter while following the tutorial, along with likely causes and how to fix them.  Use the symptom index to quickly find the issue you’re facing.  For more details, refer to the relevant chapter.

## Symptom index

| Symptom | Likely root cause | Fix | Stage | More info |
|---|---|---|---|---|
| **Invalid or expired token** | Bot token is missing, expired, or revoked. | Double‑check `.env`; obtain a new token from BotFather; rotate token if leaked. | 1–3 | [Token safety](02-botfather-and-token-safety.md) |
| **Missing token / environment variable** | `.env` not loaded or `BOT_TOKEN` undefined. | Ensure `dotenv` loads the file; activate the virtualenv; rename `.env.example` to `.env`. | 1–3 | [Setup](01-absolute-zero-setup.md) |
| **Wrong chat ID** | Using an incorrect chat ID in API calls. | Use `update.message.chat_id` instead of hardcoding IDs; test in private chat first. | Various | [Commands](06-commands-and-handlers.md) |
| **Bot cannot message user first** | Bots cannot initiate conversations. | Ask the user to start the bot via `/start` or by sending any message. | All | [Bot API docs](03-bot-api-fundamentals.md) |
| **Webhook already set / polling conflict** | Webhook is still active when using polling. | Delete the webhook before `run_polling()`; use `drop_pending_updates=True` only if you intentionally want to discard queued updates. | 5–10 | [Polling vs Webhooks](05-polling-vs-webhooks.md) |
| **Duplicate updates / offset mistake** | Manual polling with wrong offset or using polling after webhooks. | Use `run_polling()` to handle offsets automatically; reset the webhook. | 5 | [Backend reality](04-backend-reality.md) |
| **Webhook TLS/domain/port failure** | Invalid URL, HTTP instead of HTTPS, wrong port binding. | Use a valid HTTPS URL; ensure your server listens on the `PORT` env var; configure TLS. | 10 | [Hosting and deployment](10-hosting-and-deployment.md) |
| **Callback query not answered** | Missing `answer()` call in callback query handler. | Always call `await query.answer()` to acknowledge. | 7 | [Keyboards and callbacks](07-keyboards-and-callbacks.md) |
| **Group privacy mode confusion** | Bot cannot see messages in groups due to privacy settings. | Disable privacy mode in BotFather if you need to read all group messages; or ask users to prefix commands with your bot username. | 6 | [Commands and handlers](06-commands-and-handlers.md) |
| **Missing permissions/admin rights** | Bot does not have permission to send messages or receive media. | Ensure the bot is an administrator in the chat/channel; check allowed scopes in BotFather. | Various | [Security baseline](09-security-baseline.md) |
| **429 / rate limits** | Too many requests to the Bot API. | Add delays between API calls; use `await asyncio.sleep()`; avoid tight loops. | Various | [Backend reality](04-backend-reality.md) |
| **Render Free spin‑down** | Service goes to sleep after inactivity. | Use paid Starter tier or a different platform; do not rely on Free for production. | 10 | [Deployment/render.md](../deployment/render.md) |
| **Ephemeral filesystem / state loss** | Host platform wipes local storage on restart. | Use a database or PTB persistence; avoid relying on local files for critical data. | 10 | [State and persistence](08-state-and-persistence.md) |
| **Port/health check failure** | App not binding to the correct port or not responding. | Read the `PORT` env var; return 200 on `/` or `/health` routes; check logs. | 10 | [Deployment guides](../deployment/render.md) |
| **Dependency install failure** | `requirements.txt` missing, edited incorrectly, or incompatible with the interpreter. | Restore the committed requirements, run `pip install -r requirements.txt`, and keep the `python-telegram-bot[webhooks]==22.8` extra intact for the webhook example; use the tutorial's Python 3.13.x baseline or revalidate a newer interpreter against the pinned dependencies. | All | [Hosting and deployment](10-hosting-and-deployment.md) |
| **Framework version mismatch** | Using unsupported PTB version. | Keep the root requirement `python-telegram-bot[webhooks]==22.8`; upgrade only after verifying compatibility with Bot API versions and the tutorial examples. | All | [Research revalidation snapshot](../REVALIDATION_SNAPSHOT.md) |
| **Async confusion** | Forgetting `await` or mixing sync/async code. | Declare handlers with `async def`; await asynchronous functions; use `Application.run_polling()`. | 4–9 | [Backend reality](04-backend-reality.md) |
| **Markdown/HTML parse errors** | Unescaped characters causing parse errors. | Use `telegram.constants.ParseMode.HTML` or escape special characters properly. | Various | [Bot API docs](03-bot-api-fundamentals.md) |
| **Timezone/scheduling mistakes** | Using local time instead of UTC or misconfiguring cron jobs. | Use Python’s standard `datetime` and `zoneinfo`; store times in UTC; convert to user timezone when needed. | Advanced | External resources |
| **Unicode/non‑ASCII issues** | Encoding errors when sending or receiving text. | Ensure your files are UTF‑8 encoded; avoid mixing encodings; test with international characters. | All | Python docs |

## How to use this page

1. Identify the symptom that matches your issue.
2. Read the likely root cause and suggested fix.
3. Follow the link to the relevant chapter or file for detailed guidance.
4. If the problem persists, search the official [python‑telegram‑bot documentation](https://docs.python-telegram-bot.org/) or consult community forums.

Feel free to contribute additional troubleshooting entries to this page as you encounter new issues.
