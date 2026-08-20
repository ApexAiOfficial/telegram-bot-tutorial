# Use official Python runtime. 3.13-slim keeps the image small.
FROM python:3.13-slim

WORKDIR /app

# Build context is the repository root.
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY examples/10-docker/bot.py /app/bot.py
COPY .env.example /app/.env.example

CMD ["python", "bot.py"]
