# Deployment on Render (canonical)

This guide shows how to deploy your bot using the **Render** platform.  Render is the canonical hosting solution for this tutorial because it offers persistent services, managed TLS, custom domains, health checks, and simple configuration.  **Use the paid Starter tier** for production bots; the free tier is suitable only for demonstrations because services spin down after 15 minutes of inactivity and lose any local state.

## Prerequisites

* A Render account.  Sign up at [render.com](https://render.com/) if you don’t have one.
* A GitHub repository with your bot’s source code (do **not** commit `.env`).  The instructions below assume the repository has been published and connected to Render.
* A bot token from BotFather and, optionally, a list of admin user IDs. The public webhook path also requires a webhook secret.

## Step 1 – Create a new Web Service

1. Log in to the Render dashboard.
2. Click **New** → **Web Service**.
3. Connect your GitHub account and select the repository containing your bot.
4. Choose a **Name** for the service (e.g. `telegram-bot-tutorial`).  Render will generate a default domain like `telegram-bot-tutorial.onrender.com`.
5. Select **Environment** as “Python”.
6. In **Build Command**, enter:
   ```bash
   pip install -r requirements.txt
   ```
7. In **Start Command**, specify how to run your webhook server.  For example, if your bot uses `examples/11-webhook-deploy/bot.py` with PTB’s built‑in webhook server, enter:
   ```bash
   python examples/11-webhook-deploy/bot.py
   ```
   Adjust the path if your main script is elsewhere.
8. Choose the **Paid** plan (Starter).  The free plan is for demos only and will spin down.

## Step 2 – Configure environment variables

Set the following environment variables under the **Environment** section:

| Variable | Value | Notes |
|---|---|---|
| `BOT_TOKEN` | Your bot token from BotFather | Mandatory |
| `ADMIN_IDS` | Comma‑separated list of Telegram user IDs | Optional |
| `WEBHOOK_URL` | `https://<your-service-name>.onrender.com/webhook` | Must match your service’s domain and route |
| `PORT` | Automatically provided by Render (do **not** set) | PTB will pick up `PORT` if needed |
| `WEBHOOK_SECRET` | A 16-256 character random value using letters, digits, `_`, or `-` (required for this public webhook path) | Required so Telegram webhook requests are authenticated with the secret-token header |

Render automatically injects `PORT` into the environment.  Your code should read it and listen on that port when using custom servers.

## Step 3 – Configure the webhook

After your service is built and running, you need to set the webhook with Telegram.  You can do this in your code (recommended) or manually using `curl`:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -d "url=https://<your-service-name>.onrender.com/webhook" \
     -d "secret_token=<WEBHOOK_SECRET>"
```

If your bot uses PTB’s `run_webhook()` method, specify the `listen` address, `port`, `url_path`, and `webhook_url`.  Example code is provided in `examples/11-webhook-deploy/bot.py`.

## Step 4 – Health checks

Render expects your service to respond to an HTTP GET on the root path (`/`) or the path you specify in the Health Check settings.  Verify this behaviour during smoke testing.  To satisfy this, you can:

- Add a route in your framework (e.g. `aiohttp` or `Flask`) that returns `200 OK`.
- Implement and verify an explicit `/health` or `/` endpoint if your chosen web stack supports it.
- Configure Render’s **Health Check Path** to the endpoint you have actually implemented and smoke-tested.

## Step 5 – Deploy and verify

1. Click **Create Web Service**.  Render will build the image and start your bot.
2. Monitor the **Logs** tab for startup output and error messages.  Look for a message indicating that the webhook is set.
3. Send a message to your bot on Telegram.  It should respond as defined in your code.

## Limitations of the free tier

The free tier spins down after 15 minutes of inactivity.  When spun down, incoming webhook requests will fail, and your bot will not receive updates.  The local filesystem is also wiped on redeploy or spin‑down.  Use the free tier only for testing and demos; upgrade to the Starter plan for reliability.

## Troubleshooting

* **Bot doesn’t respond**: Check the webhook status using `getWebhookInfo`.  Ensure the URL is correct and uses `https://`.
* **502/504 errors**: Your bot may be listening on the wrong port.  Ensure your code reads the `PORT` environment variable or uses PTB’s `run_webhook` which defaults to `PORT`.
* **Webhook fails with timeout**: The bot must respond quickly (<5 seconds).  Long tasks should be offloaded to background jobs.
* **Secret token mismatch**: If you set a `WEBHOOK_SECRET`, verify that your code checks the `X‑Telegram‑Bot‑Api‑Secret-Token` header.

For additional assistance, consult Render’s [official documentation](https://docs.render.com/) and the `python‑telegram‑bot` [Deployment guide](https://docs.python-telegram-bot.org/en/stable/deployment.html).


## Health checks

Do not assume arbitrary paths return HTTP 200. Configure Render's health check only to a route you have implemented and verified during smoke testing. If the selected web stack supports it, implement a minimal `/health` or `/` endpoint; otherwise use a verified route and document the expected response.
