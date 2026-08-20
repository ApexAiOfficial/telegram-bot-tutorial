# 04 – Backend Reality

## What you will build

In this chapter you will look under the hood of your bot.  You will not change any behaviour from the previous stage, but you will learn how the **python‑telegram‑bot** framework runs your code, how updates are dispatched, and why asynchronous programming is important.  Understanding the runtime model will help you design more advanced bots later.

## Why this concept exists

When a bot receives an update from Telegram, the framework must parse it, decide which handler should run, execute that handler, and then send the result back to Telegram.  This process can happen many times per second, and long‑running operations may block other handlers unless you use asynchronous code.  Knowing the backend reality helps you avoid pitfalls like blocking the event loop or mixing polling and webhooks.

## Prerequisites

* Complete Stage 3 (Bot API fundamentals) and have a working echo bot.
* Familiarity with Python functions and basic async/await syntax.  You do not need to be an async expert.

## Concepts/files involved

* `Application` – orchestrates the event loop and dispatcher.
* `Dispatcher` – routes updates to handlers based on filters.
* `Context` – object that carries per‑update state and helps schedule background jobs.
* `async` handlers – functions defined with `async def` that can await other coroutines.

You will inspect the code from the previous stage to see where these components fit in.

## Exploring the runtime

1. Open your `examples/01-echo-bot/bot.py` file.  Notice the following line:
   ```python
   application = Application.builder().token(TOKEN).build()
   ```
   This builder creates an `Application` instance.  Internally it sets up an **event loop** using Python’s `asyncio` library.  All handlers run on this loop.
2. Each call to `application.add_handler(...)` registers a **handler**.  A handler is a function that will be called when a certain type of update arrives (e.g. a command or a text message).
3. Finally `application.run_polling()` starts the loop.  For each new update, the dispatcher looks at its list of handlers, finds the first one whose filter matches, and schedules it to run.

### Asynchronous handlers

Handlers defined with `async def` can `await` other asynchronous functions without blocking the event loop.  For example, if your bot makes an HTTP request to another API, it should `await` the request so other handlers can run concurrently.  All examples in this tutorial use async handlers.

### Concurrency pitfalls

- **Blocking code**: Avoid long `sleep` calls or CPU‑heavy loops inside handlers.  Blocking the event loop delays handling of other messages.
- **Shared state**: If you store data in a global variable, make sure to handle concurrent access.  For simple bots we use local variables or context to avoid race conditions.
- **Mixing polling and webhooks**: Only one transport (polling or webhook) can be active at a time.  If you call `run_polling()` and then set a webhook, Telegram will continue sending updates to your webhook endpoint but your bot will still poll, causing duplicate updates.  Always remove the webhook when you switch to polling and vice versa.

## What just happened

By reading through your own code and the framework docs, you gained a mental model of how updates move through the event loop and dispatcher.  You also learned why asynchronous code matters and how to avoid common concurrency pitfalls.

## Common mistakes

- **Running blocking functions** inside handlers.  If you must call a blocking function, wrap it in a thread or process executor using `Application.run_async`.
- **Creating multiple applications** in the same process.  Only one `Application` should run at a time.
- **Expecting sequential execution** of handlers.  The dispatcher may run multiple handlers concurrently; do not assume order unless you set `block=False` and handle concurrency explicitly.

## Troubleshooting links

If your bot hangs or becomes unresponsive:

- Check for synchronous network requests or database calls inside handlers.  Convert them to asynchronous if possible.
- Look for exceptions in the console; unhandled exceptions can stop the event loop.
- Ensure you are not mixing polling and webhook transports at the same time.

## Where it fits in the lifecycle

This chapter adds detail to the backend part of the mental model: **Update → Dispatcher → Handler → App logic**.  Understanding this helps you design robust bots.

## Next step

Move on to [05 – Polling vs Webhooks](05-polling-vs-webhooks.md) to compare the two transports and learn when to use each.
