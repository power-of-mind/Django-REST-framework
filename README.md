# 🏠 Smart Home API

REST API для системы умного дома, построенный на Django REST Framework.

## 📋 Описание

Проект представляет собой бэкенд-приложение для управления устройствами умного дома через REST API.

Система позволяет:

* Получать информацию об устройствах
* Отслеживать текущее состояние устройств
* Управлять устройствами через HTTP-запросы
* Использовать встроенный интерфейс Django REST Framework для тестирования API

---

## 🛠 Технологии

* Python 3.x
* Django
* Django REST Framework (DRF)
* SQLite (по умолчанию)

---

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/power-of-mind/Django-REST-framework.git
cd Django-REST-framework
```

### 2. Создание виртуального окружения

#### Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install django djangorestframework
```

### 4. Применение миграций

```bash
cd smart_home
python manage.py migrate
```

### 5. Создание суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запуск сервера

```bash
python manage.py runserver
```

После запуска API будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

---

## 📁 Структура проекта

```text
Django-REST-framework/
└── smart_home/
    ├── manage.py
    ├── smart_home/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── ...
```

### Основные файлы

| Файл          | Назначение                   |
| ------------- | ---------------------------- |
| `manage.py`   | Управление проектом Django   |
| `settings.py` | Настройки приложения         |
| `urls.py`     | Маршрутизация URL            |
| `wsgi.py`     | Точка входа для WSGI-сервера |

---

## 🔌 API Endpoints

После запуска сервера браузируемый интерфейс Django REST Framework будет доступен по адресу:

```text
http://127.0.0.1:8000/
```

### Пример запроса без авторизации

```bash
curl -H "Accept: application/json" http://127.0.0.1:8000/
```

### Пример запроса с авторизацией

```bash
curl -u admin:password http://127.0.0.1:8000/
```

---

## 🔐 Авторизация

Проект использует стандартные механизмы аутентификации Django REST Framework.

Панель администратора доступна по адресу:

```text
http://127.0.0.1:8000/admin/
```

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT**.

---

## 🤝 Вклад в проект

Если вы хотите внести изменения в проект:

1. Сделайте форк репозитория.
2. Создайте новую ветку:

```bash
git checkout -b feature/my-feature
```

3. Зафиксируйте изменения:

```bash
git commit -m "Add my feature"
```

4. Отправьте ветку в удалённый репозиторий:

```bash
git push origin feature/my-feature
```

5. Создайте Pull Request.

---

⭐ Если проект оказался полезным, поставьте ему звезду на GitHub.
