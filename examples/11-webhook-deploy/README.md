# 11 – Webhook Deployment

This example runs the bot with an **authenticated webhook** instead of long polling. The public webhook path requires `BOT_TOKEN`, `WEBHOOK_URL`, `WEBHOOK_SECRET`, and `PORT` (or the default local port). If `WEBHOOK_SECRET` is missing, startup fails closed.

The canonical `requirements.txt` installs `python-telegram-bot[webhooks]==22.8`, which includes PTB's webhook runtime dependency.

## Local webhook test with ngrok

```bash
export BOT_TOKEN=your_token
export WEBHOOK_URL=https://your-ngrok-host.example/webhook
export WEBHOOK_SECRET='use_a_long_random_secret_1234'
export PORT=8443
python examples/11-webhook-deploy/bot.py
```

PTB's `run_webhook()` receives the full public `webhook_url` and `secret_token`, so it can register the webhook itself. You do not need a second manual `setWebhook` call when using this path.

## Deploying to a PaaS

Set the same four values in the platform's secret/environment-variable UI. The service must listen on the platform-provided `PORT` and on `0.0.0.0` where the platform requires it. See the provider-specific deployment guides.

## Common mistakes

- Omitting the webhook path from `WEBHOOK_URL`.
- Leaving `WEBHOOK_SECRET` blank; this example intentionally refuses to start.
- Binding to localhost or a hard-coded port when the platform injects `PORT`.
- Trying to use long polling while a Telegram webhook is still configured.
