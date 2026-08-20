# 10 – Hosting and Deployment

## What you will build

In this chapter you will prepare to deploy your bot beyond your local machine.  You will not deploy yet (that comes in the deployment guides), but you will learn how to package your bot for deployment, choose a hosting platform, configure environment variables, and set up a webhook.  You will also learn why we recommend **Render’s** paid tier for the canonical tutorial path and why free tiers are only suitable for demonstration.

## Why this concept exists

To share your bot with the world you must run it on a publicly accessible server.  Hosting providers vary widely in pricing, reliability, and ease of use.  Without guidance, beginners may pick a platform that is unreliable or has hidden limitations.  This chapter summarises your options and lays the groundwork for the deployment guides in the `deployment/` folder.  For a scannable platform matrix, see the [Hosting Comparison Matrix](comparisons.md#hosting-comparison-matrix).

## Prerequisites

* Complete Stage 9 (Security baseline).  Ensure your `.env` is configured and `.env.example` is committed without secrets.
* Familiarity with webhooks from Stage 5.

## Concepts/files involved

* `requirements.txt` – lists dependencies for the bot.  Hosting providers use this to install packages.
* `Dockerfile` (in later examples) – describes containerised deployment.  Only required if you choose Docker‑based hosting.
* Environment variables – used for `BOT_TOKEN`, `WEBHOOK_URL`, `ADMIN_IDS`, etc.
* `deployment/` guides – detailed instructions for each hosting platform.

## Choosing a platform

The research behind this tutorial recommends the following priorities:

1. **Render (paid tier)** – recommended canonical choice.  It offers persistent servers, managed TLS, custom domains, health checks, and straightforward webhook configuration.  The free plan is suitable only for demos because services spin down after inactivity and the local filesystem is lost on restart.
2. **Railway** – good alternative if you prefer a different UI or pricing structure.  It supports web services, background/worker processes, managed public domains, and both polling/webhook architectures depending on service type.
3. **DigitalOcean App Platform** – another viable option with similar features.  Pricing may be higher and free credits expire.
4. **VPS (e.g. Hetzner Cloud)** – offers full control with a virtual server.  Suitable for advanced users comfortable managing Linux, firewalls, TLS certificates, and reverse proxies like Nginx.
5. **Fly.io** – comparison only.  Suitable for small projects but limited free tier and region selection.
6. **Serverless platforms (AWS Lambda, Vercel Functions)** – not recommended for the first beginner deployment because function packaging, request handling, and platform limits add complexity. Webhooks themselves are request-based and can fit HTTP functions.

## Preparing your bot

Follow these steps before deploying to any platform:

1. **Clean up your code**: remove debug prints and hardcoded tokens.  Ensure all secrets come from environment variables.
2. **Install the committed dependencies** with `pip install -r requirements.txt`. Keep the tutorial's direct requirements explicit—especially `python-telegram-bot[webhooks]==22.8`, because the `[webhooks]` extra is required by the public webhook example. Do not overwrite this curated file with a blind `pip freeze`.
3. **Set environment variables**: decide how each platform stores variables and how to provide them (UI, CLI, or config file).  At minimum set `BOT_TOKEN`. For the tutorial's public webhook path also set `WEBHOOK_URL` and a non-empty `WEBHOOK_SECRET`. For admin commands, set `ADMIN_IDS`.
4. **Configure the webhook**: after deployment, your bot must call `setWebhook(url=WEBHOOK_URL, secret_token=WEBHOOK_SECRET)` to register the endpoint with Telegram.  Some frameworks (including PTB) let you specify webhook settings in `run_webhook()`.
5. **Health checks**: many platforms expect your service to expose a `/` or `/health` endpoint that returns `200 OK`. Do not assume an arbitrary path returns HTTP 200. For public deployments, explicitly verify the health-check path during smoke testing. If your chosen web stack supports a health route, implement and test a minimal `/health` or `/` endpoint. Otherwise, configure the platform health check to target a verified route. Do not rely on undocumented default unmatched-route behaviour from PTB's built-in webhook server.

## Deployment guide overview

Each file in the `deployment/` directory provides platform‑specific instructions.  They include:

- Required environment variables and where to set them.
- Step‑by‑step UI/CLI instructions to create and configure the service.
- How to set the webhook using PTB or the Bot API directly.
- Notes on free vs. paid tiers and limitations (e.g. spin‑down on free plans, persistent storage, container size).
- Troubleshooting tips for common deployment issues.

See [deployment/render.md](../deployment/render.md) for the canonical deployment path.

## What just happened

You reviewed the hosting landscape and learned what to do before deploying.  You now know why we choose a paid Render tier for reliability, and why free/demo tiers are not suitable for always-on public bots.  With these preparations you are ready to follow a specific deployment guide.

## Common mistakes

- **Using free/demo hosting for always-on service**: spin‑down and loss of data make demo tiers unreliable.
- **Forgetting to set `WEBHOOK_URL`**: without the correct external URL your bot will not receive updates.
- **Not enabling TLS**: webhooks require HTTPS.  Ensure your platform provides a certificate or you supply one.
- **Hardcoding ports**: many platforms expect you to listen on the port provided by the environment (e.g. `PORT` environment variable).

## Troubleshooting links

If your deployment does not receive updates:

- Use `getWebhookInfo` via `curl` or Telegram API to see webhook errors.
- Check platform logs for startup failures or port binding errors.
- Ensure that the firewall/security groups allow inbound HTTPS traffic on the correct port.

## Where it fits in the lifecycle

Hosting and deployment move you from local development to a public server.  The rest of the lifecycle (handlers, state, logic) remains the same.

## Next step

Proceed to [11 – Capability Map](11-capability-map.md) to explore what else the Telegram Bot API offers and plan your next features.

## Health-check guidance

Do not assume an arbitrary path returns HTTP 200.  For public deployments, explicitly verify the health-check path during smoke testing.  If your chosen web stack supports a health route, implement and test a minimal `/health` or `/` endpoint.  Otherwise, configure the platform health check to target a route that you have verified.  Do not rely on undocumented default unmatched-route behaviour from PTB's built-in webhook server.
