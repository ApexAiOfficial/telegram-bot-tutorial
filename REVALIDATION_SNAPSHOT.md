# Revalidation Snapshot — 2026-08-15

Timezone context: Eastern Time, United States.

This snapshot records materially volatile external claims rechecked on **August 15, 2026** against primary project/platform documentation. Re-run this bounded check before a later public release.

| Item | Checked value | Primary evidence | Publication note |
|---|---|---|---|
| **Telegram Bot API** | **10.2**, released **2026-07-14** | [Telegram Bot API changelog](https://core.telegram.org/bots/api-changelog) | Telegram 10.2 is newer than PTB 22.8's native Bot API support level. |
| **python-telegram-bot (PTB)** | **v22.8; native Bot API 10.0 support** | [PTB v22.8 documentation](https://docs.python-telegram-bot.org/en/v22.8/) | The tutorial intentionally pins 22.8. Do not imply it natively exposes every Bot API 10.2 feature. |
| **PTB webhook runtime** | `python-telegram-bot[webhooks]==22.8` | [PTB optional dependencies](https://docs.python-telegram-bot.org/en/v22.8/) | The `webhooks` extra is required for `Application.run_webhook()`; the canonical requirements include it. |
| **aiogram (comparison)** | **3.30.0; Bot API 10.2 support** | [aiogram 3.30.0 docs/changelog](https://docs.aiogram.dev/en/v3.30.0/changelog.html) | Comparison only; not used by hands-on examples. |
| **grammY (comparison)** | **Bot API 10.2 support** | [grammY documentation](https://grammy.dev/) | Comparison only; not used by hands-on examples. |
| **Python baseline** | Tutorial baseline remains **3.13.x** | [PTB v22.8 changelog](https://docs.python-telegram-bot.org/en/v22.8/changelog.html) | PTB's v22.8 lineage includes Python 3.14 final in its test suite; 3.13 remains a conservative tutorial baseline, not a PTB maximum-support claim. |
| **Railway** | Recurring **Free** plan after trial; web services must bind `0.0.0.0` and use injected `PORT` | [Railway plans](https://docs.railway.com/pricing/plans); [Railway networking troubleshooting](https://docs.railway.com/networking/troubleshooting/application-failed-to-respond) | Railway remains a comparison path. Free-plan resources are limited and current pricing/limits should be checked before relying on them. |
| **DigitalOcean App Platform** | App Platform starter domain is `*.ondigitalocean.app`; free App Platform tier is for static-site-only apps | [App Platform domains](https://docs.digitalocean.com/products/app-platform/how-to/manage-domains/); [App Platform pricing](https://docs.digitalocean.com/products/app-platform/details/pricing/) | A Python Telegram webhook is a dynamic service and therefore requires paid compute under current pricing. |

The revalidation confirms the tutorial's core architecture remains sound after correction: PTB 22.8 is the pinned beginner framework, polling remains the local-development default, and the canonical public PaaS lane uses an authenticated webhook. Platform/framework capability claims above are intentionally dated because they can change.
