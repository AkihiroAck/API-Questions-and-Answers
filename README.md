# API-Questions-and-Answers (Docker)

Этот проект — простое API для работы с вопросами и ответами.  
Реализован на **Django**, с использованием **PostgreSQL** и запускается через **Docker Compose**.

---

## Оглавление
1. [Возможности](#Возможности)
2. [Методы API](#Методы-API)
3. [Модели](#Модели)
4. [Установка и запуск](#Установка-и-запуск)

---

## Возможности

- Создание вопросов
- Получение списка вопросов
- Просмотр вопроса и связанных ответов
- Удаление вопросов (каскадное удаление ответов)
- Добавление и просмотр ответов
- Удаление ответов

---

## Методы API

### Вопросы
- `GET /questions/` — список всех вопросов  
- `POST /questions/` — создать новый вопрос  
- `GET /questions/{id}` — получить вопрос и все его ответы  
- `DELETE /questions/{id}` — удалить вопрос (вместе с ответами)


### Ответы
- `POST /questions/{id}/answers/` — добавить ответ к вопросу  
- `GET /answers/{id}` — получить конкретный ответ  
- `DELETE /answers/{id}` — удалить ответ

---

## Модели

### Question (Вопрос)
- `id: int`
- `text: str` — текст вопроса
- `created_at: datetime`

### Answer (Ответ)
- `id: int`
- `question_id: int` — ссылка на `Question`
- `user_id: str` — идентификатор пользователя (UUID)
- `text: str` — текст ответа
- `created_at: datetime`

---

## Установка и запуск

### 1. Клонировать репозиторий
```
git clone https://github.com/AkihiroAck/API-Questions-and-Answers.git
cd project-name
```

### 2. Создать файл .env

Создать файл **.env** в корневой папке (рядом с `docker-compose.yml`).

Пример:
```
SECRET_KEY=django-insecure-hfg!!_=%#)1=7x45ohr2481exc7ke805%ur#c!9mz$u31ibd9_
POSTGRES_ENGINE=django.db.backends.postgresql
POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Собрать и запустить контейнеры

```
docker-compose build --no-cache
docker-compose up
```

После запуска:
- API доступно по адресу: http://localhost:8000
- База данных: localhost:5432
