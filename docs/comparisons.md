# Comparisons Reference

Checked-date context: **2026-08-15**. Revalidate every framework, hosting, and storage decision before publication or major release. This file is a decision aid, not a replacement for the staged tutorial.

## Framework Comparison Matrix

v1 recommendation: use **Python + python-telegram-bot v22.8** because it best fits beginner readability, this repo's Python-first scope, and the local polling-first path.

| Framework | Language | Current status / support posture | Beginner fit | Async exposure | Documentation quality | Example quality | Deployment fit | v1 recommendation | Notes / revalidation need |
|---|---|---|---|---|---|---|---|---|---|
| **python-telegram-bot** | Python | v22.8 docs state native Telegram Bot API 10.0 support. | Strong | Moderate; modern PTB uses async handlers but hides much complexity. | Strong | Strong | Strong for polling and webhook deployments. | **Primary v1 stack.** | Recheck Bot API support before release; Telegram Bot API 10.2 currently outpaces v22.8's native Bot API 10.0 support; use only PTB surfaces actually provided by 22.8. |
| **aiogram** | Python | 3.30.0 docs indicate Bot API 10.2 support. | Moderate | High; explicit async-first framework. | Strong | Good | Strong for advanced async bots. | Comparison only. | Good future upgrade path for advanced users, but too async-heavy for the first beginner tutorial lane. |
| **pyTelegramBotAPI** | Python | Popular Python option; status should be revalidated before recommending. | Moderate | Lower to moderate depending on usage style. | Moderate | Moderate | Works for simple bots; deployment guidance varies by project style. | Not selected for v1. | Recheck release activity, Bot API support, and docs freshness before adding examples. |
| **grammY** | TypeScript / JavaScript | Docs indicate Bot API 10.2 support. | Strong for JS/TS learners; not Python-first. | Moderate; async promises are standard in JS/TS. | Strong | Strong | Strong for Node deployments and serverless/webhook patterns. | Comparison only. | Excellent non-Python path, but outside this repository's Python v1 scope. |
| **Telegraf** | TypeScript / JavaScript | Docs/release posture appears stale relative to Bot API 10.2 and must be revalidated. | Moderate | Moderate; JS async/promise model. | Moderate | Moderate | Common for Node bots, but check current maintenance and Bot API coverage. | Not selected for v1. | Revalidate release cadence, Bot API coverage, and issue health before recommending. |

## Hosting Comparison Matrix

v1 recommendation: use **Render paid web service** for the canonical public deployment path. Render Free is demo-grade only. Railway and DigitalOcean App Platform remain comparison/appendix options. Hetzner is an advanced VPS path. Fly.io is comparison-only. AWS Lambda / Vercel Functions are mention-only serverless paths.

| Platform | Cost/free-tier posture as checked | Polling fit | Webhook fit | HTTPS/domain handling | Sleep/cold-start risk | Docker support | Beginner difficulty | v1 recommendation | Revalidation need |
|---|---|---|---|---|---|---|---|---|---|
| **Render** | Free web services are demo-grade only because of spin-down and ephemeral filesystem risk; paid web service is the canonical path. | Acceptable for experiments, but polling on sleeping free services is unreliable. | **Strong** for paid always-on service. | Managed HTTPS for public service URLs. | Free/demo: high; paid: reduced. | Yes. | Low to moderate. | **Canonical public deployment path: paid Render web service.** | Recheck free/paid plan behavior, sleep rules, persistent disk behavior, and health-check settings. |
| **Railway** | Free plan is available after trial with limited monthly credit; not treated as an always-on production guarantee. | Possible, but not the primary lane. | Strong when configured as a web service. | Managed public URLs/HTTPS depending on current product behavior. | Plan-dependent; recheck. | Yes. | Low to moderate. | Appendix/comparison only. | Recheck pricing, sleep/cold-start behavior, and current deployment flow. |
| **DigitalOcean App Platform** | Static-site-only apps can use the free tier; a Python webhook web service requires paid compute under current pricing. | Possible via a worker/background service; webhook is the tutorial's PaaS web-service path. | Strong. | Managed HTTPS and domains. | Lower on paid services; check tier details. | Yes. | Moderate. | Appendix/comparison only. | Recheck pricing, starter limits, env-var UX, and buildpack/container options. |
| **Hetzner Cloud** | VPS billing; no managed bot-specific free tier assumed. | Strong if process is supervised. | Strong with reverse proxy and TLS. | User-managed domain, TLS, firewall, and reverse proxy. | Low if configured correctly. | Yes. | High for beginners. | Advanced VPS appendix only. | Recheck VPS pricing, regions, firewall defaults, and OS hardening steps. |
| **Fly.io** | Pricing/free allowance posture must be rechecked. | Possible, but not the beginner baseline. | Strong for containerized webhooks. | Managed HTTPS with Fly apps/domains. | Machine scaling/sleep behavior can vary by configuration. | Yes. | Moderate to high. | Comparison only. | Recheck pricing, scale-to-zero behavior, volumes, regions, and deploy workflow. |
| **AWS Lambda / Vercel Functions** | Serverless cost/free posture varies and must be rechecked. | Poor fit; polling is not natural for serverless. | Possible via HTTP functions. | Managed HTTPS endpoints. | Cold starts are expected. | Limited/indirect depending on platform. | High for beginners. | Mention-only; not canonical. | Recheck webhook timeout limits, cold starts, request validation, and background task constraints. |

## Storage / Persistence Comparison Matrix

v1 recommendation: teach **in-memory state** first, then **local file / PicklePersistence** for local persistence. Do not promote Postgres or Redis to v1 unless scope expands. Always explain ephemeral filesystem risk on demo/free hosting.

| Option | What it teaches | Persistence guarantee | Beginner difficulty | Local fit | Deployment fit | v1 recommendation | Future-work notes |
|---|---|---|---|---|---|---|---|
| **No state** | Stateless handlers, commands, and echo bots. | None. Every update stands alone. | Very low. | Excellent. | Excellent for simple bots. | Use in earliest examples. | Add state only when the bot needs memory. |
| **In-memory state** | Conversation flow and `context.user_data` concepts. | Lost on process restart. | Low. | Excellent. | Weak for production because restarts lose data. | Teach before persistence. | Good stepping stone before file or database storage. |
| **Local file / PicklePersistence** | File-backed bot/user/chat data and restart survival. | Survives local restarts if filesystem persists. | Low to moderate. | Excellent. | Risky on ephemeral filesystems; unsuitable for demo/free hosts that discard local state. | **Primary v1 persistence example.** | Explain backup, privacy, and file-permission risks. |
| **SQLite** | Relational local database basics. | Strong locally when file persists. | Moderate. | Strong. | Risky on ephemeral hosts; better on VPS or persistent disk. | Optional future enhancement. | Useful bridge between pickle and managed Postgres. |
| **Postgres** | Managed relational production storage. | Strong when managed/hosted correctly. | Moderate to high. | Requires local service or managed DB. | Strong for production. | Future work only. | Add when the tutorial expands beyond local persistence. |
| **Redis** | Fast cache/session storage and queues. | Usually memory-first with persistence options depending on config. | Moderate to high. | Requires local service. | Strong for caching, rate limiting, and queues. | Future work only. | Good for advanced state, locks, jobs, and rate-control patterns. |

## Decision Summary

- Beginner framework: **python-telegram-bot**.
- Beginner local transport: **long polling**.
- Canonical PaaS public transport in this tutorial: **webhook**. Long polling remains valid for persistent worker/VPS deployments.
- Canonical public host: **paid Render web service**.
- Beginner persistence: **local file / PicklePersistence**, with clear warnings about ephemeral filesystems.
- Advanced future storage: **Postgres** and **Redis**.
