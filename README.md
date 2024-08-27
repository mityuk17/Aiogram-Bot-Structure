# Файловая структура Telegram-бота на Aiogram3

## Реализованный функционал
- [x] Docker compose (Запуск бота, поднятие PostgreSQL, Redis)
- [x] Миграции alembic
- [x] Makefile для удобного сборкой и запуском
- [ ] Логирование

## Запуск бота
### dev-версия (синхронизация файлов и быстрый перезапуск бота с внесением изменений)
```
make build-run dev
```
### prod-версия
```
make build-run prod
```

## Используемые технологии
* Aiogram 3
  - pythoh фреймворк для работы с Telegram Bot API
* SQLmodel
  - python библиотека, объединяет sqlalchemy и pydantic в ORM-систему
* Apscheduler
  - python библиотека планировщик задач
* PostgreSQL
  - Основная база данных
* Redis
  - in-memory база данных для хранения FSM Telegram-бота
* Docker compose
  - контейнеризация проекта
* Makefile
  - Упрощение сборки проекта
