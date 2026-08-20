# 10 – Docker Intro

This example shows how to run your bot inside a Docker container.  Containerising your bot makes deployments reproducible and portable across platforms that support Docker.

## Files

| File | Purpose |
|---|---|
| `bot.py` | The bot code (echo bot with `/start`). |
| `Dockerfile` | Instructions to build a Docker image. |

## Building and running with Docker

1. Build the Docker image **from the repository root** so the Dockerfile can copy `requirements.txt` and `.env.example`:
   ```bash
   docker build -f examples/10-docker/Dockerfile -t telegram-bot-example:latest .
   ```
2. Prepare a local `.env` file at the repository root with your `BOT_TOKEN`:
   ```bash
   cp .env.example .env
   # edit .env and set BOT_TOKEN=your token
   ```
3. Run the container from the repository root, passing the environment file:
   ```bash
   docker run --env-file .env telegram-bot-example:latest
   ```
4. Send `/start` or any text to your bot to test it.

## What changed since previous examples

* Added a Dockerfile using `python:3.13-slim` as the base image.
* Installed dependencies via `pip install -r requirements.txt` within the container.
* Provided instructions to build and run the image with environment variables.

## Common mistakes

- Building from the wrong directory.  Use the documented repo-root build command with `-f examples/10-docker/Dockerfile`.
- Not passing the `.env` file when running the container; the bot will raise an error due to missing `BOT_TOKEN`.
