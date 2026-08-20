# 05 – Polling vs Webhooks

## What you will build

In this chapter you will learn the difference between **long polling** and **webhooks** for receiving updates and how hosting shape—not a blanket "production" rule—drives the choice.

## Why this concept exists

Telegram supports two mutually exclusive update-delivery mechanisms:

* **Long polling (`getUpdates`)**: your bot maintains outbound requests to Telegram. It needs no public inbound URL and works well locally, on a VPS, or in a persistent worker/background service.
* **Webhook (`setWebhook`)**: Telegram sends one HTTPS request per update to your public endpoint. It fits PaaS web services and HTTP/serverless-style deployments naturally.

This tutorial develops locally with polling and uses an authenticated webhook as its **canonical PaaS web-service deployment pattern**. That is a tutorial choice, not a Telegram requirement that production bots use webhooks.

## Prerequisites

* Complete Stage 4 (Backend reality).
* Have a working bot running with `run_polling()`.

## Concepts/files involved

* `run_polling()` – starts long polling and blocks until stopped.
* `run_webhook()` – starts PTB's webhook server and registers/accepts webhook delivery.
* Webhook URL – a publicly accessible HTTPS endpoint.
* Webhook secret token – required by this tutorial's public webhook path so Telegram requests can be authenticated with the secret-token header.

## Polling

Polling is ideal for local development and also valid in production where the host supports a persistent worker/background process. It avoids public ingress entirely, which can simplify deployment.

Use polling when, for example:

1. developing locally;
2. running a supervised bot process on a VPS;
3. using a PaaS worker/background-service type that does not need HTTP ingress.

## Webhooks

With webhooks, Telegram sends an HTTPS POST for each update. Use a webhook when your hosting model is an HTTP web service or function and public ingress is the natural fit.

For this tutorial's public webhook lane:

- use HTTPS;
- bind the application to the host/port required by the platform;
- set a strong `WEBHOOK_SECRET` using 16-256 letters, digits, `_`, or `-`;
- pass that value through PTB's `secret_token` parameter;
- keep handlers responsive and move long work out of the request path.

## Decision guide

| Scenario | Recommended transport |
|---|---|
| Local development | **Polling** |
| Persistent VPS process | **Polling or webhook**, depending on whether you want public ingress |
| PaaS worker/background service | **Polling** is valid |
| PaaS web service (this tutorial's canonical public lane) | **Webhook** |
| HTTP/serverless function | **Webhook** |

## Switching safely

Telegram does not use long polling while a webhook is configured. Remove the webhook before returning to polling. `drop_pending_updates=True` **deletes queued updates**, so choose it only when discarding those updates is intentional.

Example that preserves queued updates:

```python
await bot.delete_webhook(drop_pending_updates=False)
```

Use `True` only when you have deliberately decided that old queued updates should not be processed.

## Common mistakes

- Trying to use polling while a webhook is still configured.
- Treating webhooks as a universal production requirement instead of a hosting trade-off.
- Making the public webhook secret optional.
- Assuming a webhook is a persistent Telegram-to-app connection; it is request-based HTTP delivery.

## Next step

In [06 – Commands and Handlers](06-commands-and-handlers.md) you will extend your bot with additional commands and filters.
