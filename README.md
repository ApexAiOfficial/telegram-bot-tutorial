# Telegram Bot Tutorial

Welcome to the **Telegram Bot Tutorial** repository. This project is a comprehensive, beginner‑friendly guide to building Telegram bots with **Python** using the `python‑telegram‑bot` framework.  It takes you from **absolute zero**—no prior Python or Telegram experience required—to a functional, deployable bot.  Along the way you will learn how the Bot API works behind the scenes, how to structure and secure your code, and how to avoid the common pitfalls that frustrate new developers.

## What you'll learn

* **Set up your environment** using Python 3.13 and a virtual environment (`venv`).
* **Create a bot** using BotFather and keep its token secret with a `.env` file and `.gitignore`.
* **Understand the Telegram Bot API** and the lifecycle of an update: from user input, through Telegram’s servers, to your backend, into a handler, through your business logic and back to the user.  The mental model introduced in `docs/00-overview-and-mental-model.md` appears in both prose and diagram form.
* **Build bots incrementally.** Start with a simple echo bot, then add command handling, inline keyboards, callback queries, conversation state, persistence and admin‑only commands.  Each stage is a runnable example in `examples/` with a corresponding tutorial chapter in `docs/`.
* **Compare long polling and webhooks** and learn when to use each.  Develop locally with polling and deploy publicly with webhooks.  See the [Comparisons Reference](docs/comparisons.md) for framework, hosting, and persistence matrices.
* **Deploy a bot** using the canonical PaaS (Render’s paid tier) with webhooks.  Learn why the free tier is demo‑grade only and why paid services or a VPS are required for reliability ([Render Free web services documentation](https://render.com/docs/free)).
* **Structure your project** for maintainability.  Stage 5 introduces a modular structure with separate handler and keyboard modules.
* **Troubleshoot common issues** using our symptom‑indexed guide in `docs/troubleshooting.md`.
* **Adopt a secure and responsible posture**: use `.env` files, protect tokens from logs, enforce admin allowlists, validate webhook secrets, respect rate limits and avoid abusive automation.

## Quickstart

The *Full Course* begins at Stage 0, but impatient readers can jump straight into a working bot:

1. **Install Python 3.13** if you don’t already have it.  Check with:
   ```bash
   python3 --version
   ```
   The tutorial uses Python 3.13.x as its baseline; Python 3.14 exists but may not yet be the default on your platform ([Python 3.14.0 release notes](https://www.python.org/downloads/release/python-3140/)).
2. **Clone this repository** and change into its directory:
   ```bash
   git clone https://github.com/ApexAiOfficial/telegram-bot-tutorial.git
   cd telegram-bot-tutorial
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Configure your environment**:
   ```bash
   cp .env.example .env
   # edit .env and set BOT_TOKEN and ADMIN_IDS
   ```
   Never commit `.env` or your real token.
6. **Run the first example**:
   ```bash
   cd examples/01-echo-bot
   python bot.py
   ```
   Start a chat with your bot in the Telegram app, send `/start` or any message, and see it echo your text.

For a structured journey, follow the [Full Course](docs/00-overview-and-mental-model.md) from Stage 0 to Stage 11.  The **Quickstart lane** summarises the essential steps, the **Reference lane** provides definitions and the **Troubleshooting lane** helps diagnose issues.

## Repository layout

```
telegram-bot-tutorial/
├── README.md               ← this file
├── LICENSE                 ← MIT license for code/software-support files
├── LICENSE-DOCS            ← CC BY 4.0 license for documentation/content
├── CHANGELOG.md            ← release history
├── REVALIDATION.md         ← revalidation policy and checked sources
├── REVALIDATION_SNAPSHOT.md← snapshot of current versions/pricing
├── .gitignore              ← ignores secrets, caches and virtual envs
├── .gitattributes          ← counts examples/ as code for GitHub's language stats
├── .env.example            ← template for environment variables
├── requirements.txt        ← Python dependencies for examples
├── docs/                   ← tutorial chapters and reference
│   ├── 00-overview-and-mental-model.md
│   ├── 01-absolute-zero-setup.md
│   ├── 02-botfather-and-token-safety.md
│   ├── 03-bot-api-fundamentals.md
│   ├── 04-backend-reality.md
│   ├── 05-polling-vs-webhooks.md
│   ├── 06-commands-and-handlers.md
│   ├── 07-keyboards-and-callbacks.md
│   ├── 08-state-and-persistence.md
│   ├── 09-security-baseline.md
│   ├── 10-hosting-and-deployment.md
│   ├── 11-capability-map.md
│   ├── comparisons.md
│   ├── glossary.md
│   ├── troubleshooting.md
│   └── diagrams/
│       ├── update-lifecycle.mmd
│       ├── polling-vs-webhook.mmd
│       ├── handler-routing.mmd
│       ├── conversation-state.mmd
│       ├── project-structure.mmd
│       ├── deployment-decision-tree.mmd
│       └── webhook-diagnostics.mmd
├── examples/               ← runnable bots for each stage
│   ├── 01-echo-bot/
│   ├── 02-commands/
│   ├── 03-inline-keyboard/
│   ├── 04-callback-queries/
│   ├── 05-structured-handlers/
│   ├── 06-simple-state/
│   ├── 07-persistence/
│   ├── 08-admin-command/
│   ├── 09-logging-errors/
│   ├── 10-docker/
│   ├── 11-webhook-deploy/
│   └── 12-capstone/
├── deployment/             ← hosting guides (Render canonical)
│   ├── render.md
│   ├── railway.md
│   ├── digitalocean-app-platform.md
│   └── vps-generic.md
└── qa/
    └── smoke-test-checklist.md
```

## Responsible use

This repository teaches **legitimate** bot development.  It does *not* cover or endorse:

- Spam or unsolicited marketing.
- Terms‑of‑Service evasion.
- Scraping misuse or credential abuse.
- Rate‑limit bypass or bot‑to‑bot loops.
- Abusive automation.

Respect Telegram’s policies and your users’ privacy.  When exploring advanced capabilities such as Mini Apps, Web Apps or payments, remember that these features are **future‑work only** in this tutorial.

## Contributing and maintenance

Contributions are welcome.  Before proposing changes, read `REVALIDATION.md` for the version‑checking policy.  Volatile claims (framework versions, pricing, API support) carry a **checked‑date**; contributors must re‑verify them.  A quarterly recheck is recommended, and a complete revalidation is required before any public release.

## License

Copyright (c) 2026 ApexAiOfficial.

This repository uses split licensing:

- **Code and software-support files** are licensed under the **MIT License** (SPDX: `MIT`). This includes Python source files, `Dockerfile`, `requirements.txt`, `.env.example`, and `.gitignore`. See [`LICENSE`](LICENSE).
- **Documentation and educational content** are licensed under the **Creative Commons Attribution 4.0 International license (CC BY 4.0)** (SPDX: `CC-BY-4.0`). This includes Markdown files and Mermaid (`.mmd`) diagrams throughout the repository, including `README.md`, `docs/`, `deployment/`, `qa/`, example READMEs, `CHANGELOG.md`, `REVALIDATION.md`, and `REVALIDATION_SNAPSHOT.md`. See [`LICENSE-DOCS`](LICENSE-DOCS).

Unless a file states otherwise, the classification above controls.
