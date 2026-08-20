# Deployment on DigitalOcean App Platform (comparison)

DigitalOcean App Platform is an optional managed-PaaS path for the tutorial's webhook example.

## 1. Create the app

1. In DigitalOcean, create an **App** from the GitHub repository.
2. Configure a Python **web service** with build command `pip install -r requirements.txt`.
3. Set the run command to `python examples/11-webhook-deploy/bot.py`.
4. Choose a paid web-service size appropriate to the bot. DigitalOcean's current free App Platform tier is for static-site-only apps; a Python webhook service uses dynamic compute.

## 2. Environment variables

After the first deployment, App Platform assigns a starter domain on `ondigitalocean.app`. Set:

| Key | Value | Notes |
|---|---|---|
| `BOT_TOKEN` | BotFather token | Required |
| `WEBHOOK_URL` | `https://<assigned-app>.ondigitalocean.app/webhook` | Required; use the actual starter/custom domain shown by App Platform |
| `WEBHOOK_SECRET` | 16-256 random letters/digits/`_`/`-` characters | **Required for this public webhook path** |
| `ADMIN_IDS` | Comma-separated admin IDs | Optional |
| `PORT` | Platform/service port when explicitly configured | The example reads `PORT`; keep it consistent with the App Platform service configuration |

DigitalOcean documents `*.ondigitalocean.app` as the App Platform starter-domain family. `digitaloceanspaces.com` is not an App Platform ingress domain. See [App Platform domain documentation](https://docs.digitalocean.com/products/app-platform/how-to/manage-domains/).

## 3. Webhook registration

PTB's `run_webhook()` receives `WEBHOOK_URL` and `WEBHOOK_SECRET` and can register the webhook during startup. Verify with Telegram `getWebhookInfo` after deployment.

## Pricing note (checked 2026-08-15)

DigitalOcean currently provides a free App Platform tier for apps composed only of static-site components. Web services/workers/jobs use paid compute. Recheck [App Platform pricing](https://docs.digitalocean.com/products/app-platform/details/pricing/) before deployment.

## Troubleshooting

- **App does not start:** inspect build/runtime logs and confirm `requirements.txt` installs successfully.
- **Webhook does not trigger:** verify the actual `ondigitalocean.app` or custom domain, HTTPS, `/webhook`, and secret.
- **Port mismatch:** make the configured service port and `PORT` value agree.
