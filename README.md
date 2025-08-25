# 📋 Habit Tracker - MVP веб-приложение

Полнофункциональное веб-приложение для отслеживания привычек, разработанное в качестве pet-проекта для демонстрации навыков fullstack разработки.

## 🚀 Стек технологий

*   **Backend:** Python 3, Django 4.1.7, Django REST Framework
*   **Frontend:** Vue.js 3, Pinia (State Management), Vue Router, Axios
*   **База данных:** PostgreSQL 13
*   **Аутентификация:** Django Token Authentication
*   **Окружение:** Docker, Docker Compose
*   **Дополнительно:** django-extensions, django-cors-headers

## ✨ Основные возможности (MVP)

*   🔐 **Регистрация и аутентификация** пользователей с Token-based авторизацией
*   📝 **CRUD операции с привычками** (создание, просмотр, редактирование, удаление)
*   ✅ **Отметка выполнения** привычек с возможностью отмены
*   📊 **Персональный список** привычек для каждого пользователя
*   🌐 **Полностью русифицированный** пользовательский интерфейс
*   📱 **Адаптивный дизайн** для работы на всех устройствах

## Начало работы

Для запуска проекта на вашем локальном компьютере потребуется установленный Docker и Docker Compose.

### Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Cherten/habit-tracker.git
    cd habit-tracker
    ```

2.  **Запустите проект с помощью Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    Эта команда соберет образы для backend и frontend, создаст контейнер с базой данных PostgreSQL и запустит все сервисы.

3.  **При первом запуске выполните миграции базы данных:**
    ```bash
    docker-compose run --rm backend python manage.py migrate
    ```

4.  **Приложение будет доступно по адресам:**
    *   **Frontend (клиентская часть):** [http://localhost:5173](http://localhost:5173)
    *   **Backend API:** [http://localhost:8000/api](http://localhost:8000/api)
    *   **Django Admin:** [http://localhost:8000/admin](http://localhost:8000/admin)

5.  **Чтобы остановить приложение, нажмите `Ctrl+C` в терминале и выполните:**
    ```bash
    docker-compose down
    ```

### Дополнительные команды

*   **Создание суперпользователя для Django Admin:**
    ```bash
    docker-compose run --rm backend python manage.py createsuperuser
    ```

*   **Просмотр логов:**
    ```bash
    docker-compose logs backend  # Логи бэкенда
    docker-compose logs frontend # Логи фронтенда
    ```

*   **Запуск тестов:**
    ```bash
    docker-compose run --rm backend python manage.py test
    ```

## 📂 Структура проекта

```
habit-tracker/
├── backend/                  # Django проект (API)
│   ├── core/                # Основные настройки Django
│   ├── habits/              # Приложение управления привычками
│   ├── accounts/            # Приложение аутентификации
│   ├── requirements.txt     # Python зависимости
│   └── Dockerfile          # Docker образ для бэкенда
├── frontend/                # Vue.js проект (SPA)
│   ├── src/
│   │   ├── components/     # Vue компоненты
│   │   ├── views/          # Страницы приложения
│   │   ├── stores/         # Pinia хранилища состояния
│   │   ├── router/         # Конфигурация роутинга
│   │   └── services/       # API клиент (axios)
│   ├── package.json        # Node.js зависимости
│   └── Dockerfile         # Docker образ для фронтенда
├── .gitignore             # Исключения для Git
├── docker-compose.yml     # Оркестрация контейнеров
└── README.md             # Документация проекта
```

## 🛠 API Endpoints

### Аутентификация
- `POST /api/register/` - Регистрация пользователя
- `POST /api/login/` - Вход в систему (получение токена)

### Привычки
- `GET /api/habits/` - Получить список привычек пользователя
- `POST /api/habits/` - Создать новую привычку
- `DELETE /api/habits/{id}/` - Удалить привычку
- `POST /api/habits/{id}/complete/` - Отметить привычку как выполненную
- `POST /api/habits/{id}/uncomplete/` - Отменить отметку выполнения

## 🧪 Тестирование

Проект включает unit-тесты для Django API:

```bash
# Запуск всех тестов
docker-compose run --rm backend python manage.py test

# Запуск тестов конкретного приложения
docker-compose run --rm backend python manage.py test habits
```

## 👨‍💻 Технические особенности

*   **REST API** архитектура с использованием Django REST Framework
*   **Token-based аутентификация** для безопасности API
*   **SPA (Single Page Application)** на Vue.js с клиентским роутингом
*   **State management** с помощью Pinia
*   **Responsive дизайн** с адаптацией под мобильные устройства
*   **Docker контейнеризация** для простого развертывания
*   **PostgreSQL** как production-ready база данных

## 📝 Примечания для разработки

*   Backend использует **TokenAuthentication** вместо JWT для упрощения
*   CORS настроен для разработки (`CORS_ALLOW_ALL_ORIGINS = True`)
*   Все тексты интерфейса локализованы на русский язык
*   Проект готов для расширения дополнительными функциями

## 👤 Автор

**Artyom Khalturin** - [GitHub: @Cherten](https://github.com/Cherten)

---

*Проект разработан в качестве демонстрации навыков fullstack разработки для технического собеседования.*
