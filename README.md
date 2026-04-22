# SQLMentor Bot

A lightweight, Dockerized Telegram bot that helps you learn SQL through interactive exercises with instant feedback, explanations, and progress tracking.

## Features

- 🟢 **Beginner**, 🟡 **Intermediate**, 🔴 **Advanced** levels
- **90 hand-picked SQL exercises** with schemas, hints, and explanations
- 📝 **Quick Quiz** — multiple-choice test mode with 10 random questions
- Clean button-based UX (no memorizing commands)
- SQLite-based progress tracking (persistent across restarts)
- Single-command Docker deployment

## Quick Start

1. **Create a bot** with [@BotFather](https://t.me/botfather) and copy the token.

2. **Set the token** in the environment:
   ```bash
   cp .env.example .env
   # edit .env and paste your TELEGRAM_BOT_TOKEN
   ```

3. **Run everything** with one command:
   ```bash
   docker compose up --build
   ```

That's it! Open your bot in Telegram and press `/start`.

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and open the main menu |
| `/help`  | Show help and usage tips |

## Modes

### 📚 Practice Mode
Choose a difficulty level → pick a topic → solve exercises by writing SQL queries. The bot checks your answer instantly and shows explanations.

### 📝 Quick Quiz
A fast multiple-choice test with 10 random SQL questions. Great for reviewing concepts on the go.

## Project Structure

```
.
├── bot/
│   ├── main.py       # Entrypoint
│   ├── config.py     # Settings
│   ├── handlers.py   # Commands & callback logic
│   ├── keyboards.py  # Inline button layouts
│   ├── database.py   # SQLite async helpers
│   ├── questions.py  # 90 coding exercises
│   └── quiz.py       # 25 multiple-choice questions
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example
```

## Stopping

```bash
docker compose down
```

Data is persisted in the `./data` folder via a Docker volume.
