# 09 – Security Baseline

## What you will build

In this chapter you will not write new bot features; instead, you will harden your existing code.  You will learn best practices for handling your bot token and environment variables, restricting sensitive commands to administrators, validating incoming webhook requests, and protecting user data.  A secure baseline protects your bot from abuse and accidental leaks.

## Why this concept exists

Bots can quickly become targets for abuse: leaked tokens allow attackers to hijack your bot; open administrative commands can be exploited; logging sensitive data may violate user privacy.  Security is everyone’s responsibility.  Adopting safe patterns early ensures that your tutorial doesn’t inadvertently teach harmful practices.

## Prerequisites

* Complete Stage 8 (State and persistence).
* Familiarity with `.env` files and how to load them using `python‑dotenv`.

## Key practices

### 1. Protect your bot token

Your bot’s token is essentially a password.  Follow these rules:

1. **Do not hardcode** the token in source files.  Always load it from an environment variable using `dotenv` or your hosting platform’s configuration.
2. **Add `.env` to `.gitignore`** so that your token is never committed to version control.
3. **Rotate the token** if you suspect it has been leaked.  Use BotFather’s `/revoke` command and update your environment variables.
4. For local examples, use `.env.example` to document required variables without providing real values.

### 2. Use `gitignore` wisely

Your repository includes a `.gitignore` file that ignores virtual environments, compiled files, caches, and `.env`.  Do not remove `.env` from `.gitignore`.  If you need to share an example configuration, use `.env.example` with placeholder values.

### 3. Restrict administrative commands

Sometimes you need commands that only certain users can run (e.g. `/shutdown`).  Load a list of allowed user IDs from the environment:

```python
import os
ADMIN_IDS = {int(uid) for uid in os.getenv("ADMIN_IDS", "").split(",") if uid}

async def admin_only(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorised to run this command.")
        return
    # perform the admin action
```

Provide clear instructions for adding your own Telegram user ID to `ADMIN_IDS` in `.env`.

### 4. Validate webhooks

When running a webhook you can set a **secret token** so that Telegram includes an `X‑Telegram‑Bot‑Api‑Secret-Token` header with each request.  Check this header in your code before processing the update.  This prevents random HTTP requests from being treated as updates.

### 5. Handle sensitive data carefully

Avoid logging or printing the full update payload.  If you need debugging information, log only the update type and message text, not personal details.  When storing user data, ensure it is encrypted or stored securely; do not persist tokens or sensitive credentials.

## What just happened

You learned how to establish a security baseline for your bots: keep tokens out of code, use environment variables, restrict admin commands, validate webhook requests, and avoid logging sensitive data.  These principles apply to every project you build.

## Common mistakes

- **Committing `.env`** to version control.  Always double‑check before pushing code.
- **Hardcoding admin IDs** in source files.  Instead, use environment variables.
- **Ignoring webhook headers**.  Without validating the secret token, your bot could process malicious requests.
- **Logging full updates** in production.  While convenient during debugging, it may expose private information.

## Troubleshooting links

If your bot suddenly stops responding or behaves unexpectedly:

- Check whether your token was revoked or leaked.  Rotate it if necessary.
- Ensure that `ADMIN_IDS` is correctly set and does not block legitimate commands.
- Inspect your hosting provider’s environment configuration to confirm that variables are set as expected.

## Where it fits in the lifecycle

Security is a cross‑cutting concern.  It affects every stage from the initial setup to deployment and beyond.  This chapter emphasises **responsible use** and safe handling of credentials.

## Next step

Proceed to [10 – Hosting and Deployment](10-hosting-and-deployment.md) to learn how to run your bot publicly and configure webhooks on supported platforms.
