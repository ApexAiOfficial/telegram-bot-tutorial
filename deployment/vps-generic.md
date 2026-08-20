# Deployment on a Generic VPS (advanced)

This guide explains how to deploy your bot on a **Virtual Private Server (VPS)**, such as those offered by Hetzner Cloud, DigitalOcean Droplets, or other providers.  A VPS gives you full control over the operating system, packages, and networking.  However, it requires more administrative effort.  Use this guide if you are comfortable managing Linux servers and want maximum flexibility.

## Prerequisites

* A VPS running a recent version of Ubuntu or Debian.  Allocate at least 512 MB of RAM and a small CPU core.
* A domain name (optional but recommended) pointing to your server’s IP address.
* SSH access to the server with sudo privileges.
* Your bot code cloned on the server or pulled from a private repository.
* A bot token and other environment variables.

## Step 1 – Update and install dependencies

SSH into your server and run:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip nginx
```

These commands update the package lists, install security updates, and install Python and Nginx.

## Step 2 – Clone the repository

Copy your bot’s repository onto the server.  For example:

```bash
git clone https://github.com/yourusername/telegram-bot-tutorial.git
cd telegram-bot-tutorial
```

Create a `.env` file on the server and set your `BOT_TOKEN`, `ADMIN_IDS`, `WEBHOOK_URL`, and `WEBHOOK_SECRET`.

## Step 3 – Create a virtual environment and install packages

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Pin package versions in `requirements.txt` for reproducibility.  Ensure you are using Python 3.13.x, which you may need to install manually if your distribution uses an older version.

## Step 4 – Configure Gunicorn and PTB webhook

When deploying on a VPS you can run your bot using PTB’s built‑in webhook server or behind **Gunicorn** with a minimal web framework like Flask or FastAPI.  Here is a simple approach using PTB’s `run_webhook()`:

Create `examples/11-webhook-deploy/bot.py` (if not already) that calls:

```python
application.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 8443)),
    url_path="/webhook",
    webhook_url=os.environ["WEBHOOK_URL"],
    secret_token=os.environ["WEBHOOK_SECRET"],
)
```

Set `PORT` to `8443` or another port allowed by your firewall.

## Step 5 – Configure Nginx as a reverse proxy

Use Nginx to handle TLS termination and proxy requests to your bot process:

1. Obtain an SSL certificate using **Let’s Encrypt** and **Certbot**.  For example:
   ```bash
   sudo apt install -y certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```
2. Create a new Nginx server block in `/etc/nginx/sites-available/telegram-bot`:
   ```nginx
   server {
       listen 443 ssl;
       server_name yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

       location /webhook {
           proxy_pass http://127.0.0.1:8443/webhook;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }

       location / {
           return 200 'OK';
       }
   }
   ```
3. Enable the site and reload Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/telegram-bot /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl reload nginx
   ```

This configuration forwards `/webhook` requests to your bot listening on port 8443 and returns `200 OK` for other paths (health check).

## Step 6 – Set the webhook

From your local machine or the server, call:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -d "url=https://yourdomain.com/webhook" \
     -d "secret_token=<WEBHOOK_SECRET>"
```

Telegram will send updates to your server.  Ensure that port 443 is open in your firewall (e.g. UFW).

## Maintenance and monitoring

* Use **systemd** to run your bot as a service so it automatically restarts on failure or reboot.  Create `/etc/systemd/system/telegram-bot.service` with appropriate `ExecStart` pointing to your Python script.
* Keep your system packages and Python dependencies up to date.
* Monitor logs (`journalctl -u telegram-bot.service`) for errors.
* Renew TLS certificates periodically (Certbot handles this automatically if configured).

## Notes

Deploying to a VPS offers full control but also full responsibility.  You must handle security updates, firewall rules, backups, and scalability yourself.  This path is considered **advanced** and is provided for completeness.
