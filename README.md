<div align="center">
  <h1>🍳😋CookCookhNya</h1>
  <p><strong>Your Smart Cooking Companion</strong></p>
</div>
<p align="center">
  <a href="https://t.me/cookcookhnyabot" target="_blank">
    <img src="https://img.shields.io/badge/Demo-Visit-blue?style=for-the-badge&logo=vercel" />
  </a>
</p>

> **CookCookhNya** is an innovative Telegram-based cooking assistant that transforms the way you cook by suggesting recipes based on the ingredients you already have at home. Say goodbye to the frustration of staring into your fridge, wondering what to make — CookCookhNya helps you whip up delicious meals while minimizing food waste. Perfect for students, busy professionals, and home cooks alike!
---

## 🌟 Project Overview

CookCookhNya empowers users to manage their kitchen inventory, discover tailored recipe ideas, and create shopping lists effortlessly. Built with a robust backend and an intuitive Telegram bot interface, it’s your go-to tool for smarter, more sustainable cooking.

### What It Does

- **Recipe Discovery**: Find recipes you can cook with what’s in your pantry.
- **Shopping Made Easy**: Generate lists for missing ingredients in seconds.
- **Personalized Cooking**: Save and share your own custom recipes.
- **Collaborative Features**: Share storage with housemates for group cooking.

---

## ✨ Key Features

- **Kitchen Storage Management**\
  Add, remove, and track ingredients in real-time across multiple storages.
- **Smart Recipe Finder**\
  Get recipe suggestions based on your available ingredients, even across shared storages.
- **Shopping Lists**\
  Automatically create and edit shopping lists for your chosen recipes.
- **Custom Creations**\
  Add unique ingredients and craft your own recipes to share with the community.

### Implemented Features

- ✅ Create, delete, and manage multiple storages
- ✅ Add/remove ingredients and view storage summaries
- ✅ Recipe suggestions based on single or combined storages
- ✅ Shopping list generation and management
- ✅ User profiles with custom ingredient/recipe creation and publication

---

## 🛠️ Tech Stack

### Frontend

- **Language**: C++
- **Interface**: Telegram Bot API
- **Frameworks**: TgBotStater, Boost, cpp-httplib

### Backend

- **Language**: Scala
- **Frameworks**: ZIO, Tapir, Quill, Circe
- **Database**: PostgreSQL

### DevOps

- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus (cadvisor, postgres-exporter, /metrics), Grafana, Loki, Promtail

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Telegram account and BotFather access
- Git

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Endpool/CookCookhNya.git
   ```
2. **Initialize Submodules**

   ```bash
   git submodule init && git submodule update --remote
   ```
3. **Create a Telegram Bot**
   - Visit BotFather, create a bot, and enable inline mode.
   - Copy your `BOT_TOKEN`.
4. **Configure Environment**

   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your `BOT_TOKEN`.
5. **Run the Application**

   ```bash
   docker compose up --build
   ```
6. **Access the Bot**\
   Start chatting with your bot on Telegram or check the API docs at `http://localhost:8080/docs`.

---

## 👥 Team Members

| Team Member | Telegram Alias | Email Address | Track |
| --- | --- | --- | --- |
| Maxim Fomin (Lead) | @maximf3 | m.fomin@innopolis.university | Frontend (C++) |
| Ilia Kliantsevich | @ilia852 | i.kliantsevich@innopolis.university | Frontend (C++) |
| Amirkhan Kurbanov | @s3rap1s | am.kurbanov@innopolis.university | Frontend (C++) |
| Daniel Gevorgyan | @danielambda | d.gevorgyan@innopolis.university | UI/UX + Backend |
| Vadim Ksenofontov | @Leropsis | v.ksenofontov@innopolis.university | Backend (Scala) |
| Aleksandr Gorbanev | @ben_joyce | a.gorbanev@innopolis.university | Backend (Scala) |
| Rashid Badamshin | @j0cos | r.badamshin@innopolis.university | DevOps |

---

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

## 🎉 Acknowledgments

A huge thank you to our team for their dedication and creativity in bringing CookCookhNya to life. Happy cooking! 🍽️
