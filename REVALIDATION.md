# Revalidation Policy

The Telegram Bot Tutorial aims to remain a trustworthy, up‑to‑date resource.  Many claims in this repository depend on the state of external systems (framework versions, API support levels, hosting tiers and pricing).  To avoid becoming stale, every volatile claim is annotated with a **checked‑date**.  Contributors are expected to verify and update these dates as part of routine maintenance.

## Checked‑date policy

* **Per‑claim dating:** Each table entry or paragraph that references a version number, pricing tier or feature support must include the date on which it was last verified.
* **Quarterly recheck:** We recommend a full pass through the volatile claims every **three months**.  The `REVALIDATION_SNAPSHOT.md` file records the latest check.
* **Pre‑publication recheck:** Before any new public release (e.g. a new tag or publishing the tutorial on GitHub), perform a full revalidation of all volatile claims.  Do not publish without updating checked dates.
* **Source freshness:** Always prefer primary sources.  When quoting or paraphrasing, include normal Markdown source links (not ChatGPT citation markers) so future maintainers can revisit the evidence quickly.

## Sources to recheck

At a minimum, revalidate the following items:

1. **Telegram Bot API version and recent changes**.  See the [Bot API changelog](https://core.telegram.org/bots/api-changelog) for official announcements ([Telegram Bot API changelog](https://core.telegram.org/bots/api-changelog)).
2. **python‑telegram‑bot version and Bot API support**.  Confirm the current release on [docs.python-telegram-bot.org](https://docs.python-telegram-bot.org) and ensure it supports the latest Bot API ([python-telegram-bot documentation](https://docs.python-telegram-bot.org/en/stable/)).
3. **aiogram version and support**.  Verify the README on [GitHub](https://github.com/aiogram/aiogram) notes support for the current Bot API ([aiogram README](https://github.com/aiogram/aiogram)).
4. **grammY version and support**.  Check the grammY website for claims about Bot API support ([grammY documentation](https://grammy.dev/)).
5. **Telegraf version and support** (even though it is not used here, it appears in comparison tables).
6. **Render pricing and free/starter limitations**.  The Render docs document that free web services spin down after 15 minutes and lose local filesystem state ([Render Free web services documentation](https://render.com/docs/free)).  Confirm that these details remain accurate.
7. **Railway pricing and free‑trial behaviour**.  Check Railway’s pricing documentation for the current trial credit and subsequent costs.
8. **DigitalOcean App Platform pricing and free tier**.  Confirm the existence and limitations of any starter tier.
9. **Hetzner Cloud entry pricing** for a small VPS.
10. **Fly.io pricing and runtime posture**.
11. **AWS Lambda and Vercel function limits**.  Note cold start characteristics and pricing.
12. **Python baseline**.  This repository uses Python 3.13.x; monitor whether the next stable release (e.g. Python 3.14.x) is widely available and supported by the chosen frameworks ([Python 3.14.0 release notes](https://www.python.org/downloads/release/python-3140/)).

## Updating tables and docs

When a recheck finds that a version or pricing has changed:

1. **Update the relevant table** (e.g. Framework Matrix, Hosting Matrix, compatibility matrix) with the new value and update its checked‑date.
2. **Cite the new source** next to the updated cell using the bracket citation format.  Remove or archive the old citation if it no longer applies.
3. **Update narrative text** wherever it references the old value.
4. **Record the revalidation date and summary** in `REVALIDATION_SNAPSHOT.md`.

## Maintenance responsibilities

Maintainers should schedule a quarterly review to perform these checks.  Contributors who notice stale information are encouraged to open an issue or pull request with updated evidence and citations.  Remember that unrevalidated claims can mislead beginners; accuracy is a core value of this project.