# Instructions for local development

1. Create a new directory.
2. Clone this repo
3. Run
```bash
git submodule init && git submodule update
```
4. Create a bot at [@BotFather](https://t.me/BotFather) (don't forget to enable inline mode in settings)
5. Create `.env` specifying `BOT_TOKEN` in same directory
6. Run
```bash
docker compose up --build
```
