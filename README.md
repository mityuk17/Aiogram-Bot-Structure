# Файловая структура Telegram-бота на Aiogram3

## Реализованный функционал
- [x] Docker compose (Запуск бота, поднятие PostgreSQL, Redis)
- [x] Миграции alembic
- [x] Makefile для удобного сборкой и запуском
- [ ] Логирование

## Запуск бота
### dev-версия (синхронизация файлов и быстрый перезапуск бота с внесением изменений)
```
make build-run-dev
```
### prod-версия
```
make build-run-0prod
```

## Используемые технологии
* Aiogram 3
  - Python фреймворк для работы с Telegram Bot API
* SQLmodel
  - Python библиотека, объединяет sqlalchemy и pydantic в ORM-систему
* Apscheduler
  - Python библиотека планировщик задач
* PostgreSQL
  - Основная база данных
* Redis
  - in-memory база данных для хранения FSM Telegram-бота
* Docker compose
  - Контейнеризация проекта
* Makefile
  - Упрощение сборки проекта
