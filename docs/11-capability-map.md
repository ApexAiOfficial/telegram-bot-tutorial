# 11 – Capability Map

## What you will build

This chapter is more of a reference than a hands‑on build.  You will explore the breadth of features supported by the Telegram Bot API and the **python‑telegram‑bot** framework.  You will learn what is possible beyond the basics you have implemented so far and identify areas for future learning.  This capability map helps you understand where to focus next.  For framework, hosting, and storage trade-offs, see the [Framework Comparison Matrix](comparisons.md#framework-comparison-matrix), [Hosting Comparison Matrix](comparisons.md#hosting-comparison-matrix), and [Storage / Persistence Comparison Matrix](comparisons.md#storage--persistence-comparison-matrix).

## Why this concept exists

The Telegram Bot API is rich.  It includes not only messages and commands but also media attachments, polls, games, inline queries, payments, mini apps, and more.  Beginners often feel overwhelmed or unaware of these capabilities.  A high‑level map helps you navigate and plan your learning journey.

## Prerequisites

* Complete Stage 10 (Hosting and deployment) or be familiar with the earlier stages.

## High‑level capabilities

Below is a non‑exhaustive list of features you can implement with the Telegram Bot API.  Each feature category lists examples and notes about beginner suitability.

| Category | Examples | Notes |
|---|---|---|
| **Basic messaging** | Send/receive text, markdown, HTML, photos, documents, stickers, voice messages. | Covered in this tutorial; start here. |
| **Commands** | Slash commands like `/start`, `/help`, `/settings`. | Use `CommandHandler`. |
| **Inline keyboards** | Buttons attached to messages. | Covered in Stage 7. |
| **Callback queries** | Handle button presses. | Covered in Stage 7. |
| **Custom keyboards** | Reply keyboard markup for quick replies. | Suitable for guided conversations. |
| **Conversation flows** | Manage multi‑step interactions. | Covered in Stage 8. |
| **Persistence** | Save user data across sessions. | Covered in Stage 8. |
| **Media** | Photos, audio, video, animation (GIFs). | PTB makes sending media easy. |
| **Polls and quizzes** | Create polls and multiple‑choice quizzes. | Good for interactive bots. |
| **Inline queries** | Answer queries when users type in another chat. | Advanced; not covered here. |
| **Payments / Stars** | Accept payments or tips via [Telegram Payments](https://core.telegram.org/bots/payments). | Future work; do not implement in v1. |
| **Mini apps** | Web apps and rich interactive experiences. | Advanced; explained conceptually but not implemented. |
| **Bot menus** | Global menu buttons for commands and web apps. | Requires BotFather configuration. |
| **Rich messages (10.1)** | Rich media with interactive components. | New in Bot API 10.1; advanced. |

## Future directions

As you progress beyond this tutorial, consider exploring:

- **Inline mode**: allow users to invoke your bot from any chat by typing your bot’s username and a query.
- **Polling vs Webhooks** for serverless functions: advanced users may configure AWS Lambda or Vercel to handle webhooks.
- **Integrating databases**: move from file‑based persistence to PostgreSQL or Redis for scalable storage.
- **Webhook proxies**: use services like `ngrok` to test webhooks locally without deploying.
- **Payments and mini apps**: design user flows for donations or interactive games.  Note that these features may require additional compliance and are beyond the scope of this version.

## What just happened

You mapped out the capabilities of the Telegram Bot API and the python‑telegram‑bot framework.  This overview guides you toward additional features you might build after completing the core tutorial.

## Next step

Proceed to [glossary](glossary.md) for definitions of common terms or jump to [docs/troubleshooting.md](troubleshooting.md) to prepare for debugging.  When you are ready to deploy, consult the appropriate file under `deployment/`.
