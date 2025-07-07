# TG Bot Template

Этот проект является учебным примером для создания Telegram-бота и REST-API с использованием подхода "чистой архитектуры". Бот реализован на базе aiogram 3, API работает на FastAPI, для базы данных применяется SQLAlchemy и Alembic, а управление зависимостями выполняет утилита uv. Репозиторий основан на [оригинальной версии](https://github.com/NekitPnt/TGbot_template).

## Используемые технологии

- Python 3.12
- aiogram 3
- SQLAlchemy
- Alembic
- FastAPI
- uv (управление зависимостями и запуск задач)

## Архитектура

Код разделён на несколько слоёв:

1. **Domain** – бизнес-модели и интерфейсы репозиториев.
2. **Use Cases** – приложения с бизнес-логикой бота и API.
3. **Infrastructure** – конкретные реализации репозиториев, работа с БД и Redis.
4. **Interface** – модуль бота на aiogram и веб-сервер на FastAPI.

Такое разделение облегчает тестирование и поддержку проекта.

## Установка

1. Скопируйте файл `template.env` в `.env` и заполните переменные.
2. Установите зависимости:

```bash
uv sync
```

## Запуск

### Бот

```bash
uv run python src/main_bot.py
```

### API

```bash
uv run uvicorn src.main_api:app --reload
```

### Миграции

```bash
uv run alembic upgrade head
```

### Тесты

```bash
uv run pytest tests
```

## Переменные окружения

Список основных переменных смотрите в `template.env`:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `FSM_REDIS_HOST`
- `FSM_REDIS_PORT`
- `FSM_REDIS_DB`
- `FSM_REDIS_PASS`
- `TG_BOT_TOKEN`
- `REGISTER_PASSPHRASE`
- `CREATOR_ID`

## Запуск в Docker Compose

Для локального развёртывания всех сервисов выполните:

```bash
docker-compose up --build
```

Compose автоматически использует значения из файла `.env`.