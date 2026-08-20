# Deployment on Railway (comparison)

Railway is an optional comparison path. For this tutorial, deploy the webhook example as a Railway **web service**; a separate worker/background-service architecture can also use long polling.

## 1. Create the service

1. Create a Railway project from the GitHub repository.
2. Ensure dependencies are installed with `pip install -r requirements.txt`.
3. Set the start command to `python examples/11-webhook-deploy/bot.py`.
4. Generate a Railway public domain under the service networking settings.

## 2. Environment variables

Set:

| Name | Value | Notes |
|---|---|---|
| `BOT_TOKEN` | BotFather token | Required |
| `WEBHOOK_URL` | `https://<your-railway-domain>/webhook` | Required |
| `WEBHOOK_SECRET` | 16-256 random letters/digits/`_`/`-` characters | **Required for this public webhook path** |
| `ADMIN_IDS` | Comma-separated IDs | Optional |

Do **not** hard-code `PORT`. Railway injects the `PORT` environment variable, and public web services must listen on `0.0.0.0` and that injected port. The example does both. See Railway's [application networking troubleshooting](https://docs.railway.com/networking/troubleshooting/application-failed-to-respond).

## 3. Domain and webhook

After Railway generates the public domain, set `WEBHOOK_URL` to that HTTPS domain plus `/webhook` and redeploy. PTB's `run_webhook()` registers the webhook using that URL and `WEBHOOK_SECRET`.

## Pricing note (checked 2026-08-15)

Railway currently documents a recurring **Free** plan after the trial, with limited monthly credit. Treat it as experimentation capacity rather than an always-on reliability guarantee; verify current plan limits before relying on it. See [Railway plans](https://docs.railway.com/pricing/plans).

## Troubleshooting

- **502 / service failed to respond:** confirm the process binds `0.0.0.0` and the injected `PORT`.
- **Webhook errors:** verify the generated HTTPS domain, `/webhook` path, and `WEBHOOK_SECRET`.
- **Budget/reliability:** check current Railway pricing and resource limits rather than relying on older free-tier assumptions.
