🏠 Smart Home API
REST API для системы умного дома, построенный на Django REST Framework.
📋 Описание
Проект представляет собой бэкенд-приложение для управления устройствами умного дома через REST API. Позволяет взаимодействовать с умными устройствами, получать их состояние и управлять ими через HTTP-запросы.
🛠 Технологии

Python 3.x
Django — веб-фреймворк
Django REST Framework (DRF) — построение REST API
SQLite — база данных (по умолчанию)

🚀 Установка и запуск
1. Клонирование репозитория
bashgit clone https://github.com/power-of-mind/Django-REST-framework.git
cd Django-REST-framework
2. Создание виртуального окружения
bashpython -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
3. Установка зависимостей
bashpip install django djangorestframework
4. Применение миграций
bashcd smart_home
python manage.py migrate
5. Создание суперпользователя
bashpython manage.py createsuperuser
6. Запуск сервера
bashpython manage.py runserver
API будет доступен по адресу: http://127.0.0.1:8000/
📁 Структура проекта
Django-REST-framework/
└── smart_home/          # Основное Django-приложение
    ├── manage.py
    ├── smart_home/      # Настройки проекта
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── ...              # Приложения с моделями и API
🔌 API Endpoints
После запуска сервера документация и браузируемый интерфейс DRF доступны по адресу:
http://127.0.0.1:8000/
Для взаимодействия с API можно использовать curl:
bashcurl -H 'Accept: application/json' http://127.0.0.1:8000/
Или с авторизацией:
bashcurl -u admin:password http://127.0.0.1:8000/
🔐 Авторизация
Проект использует стандартную авторизацию Django REST Framework. Войти в панель администратора можно по адресу:
http://127.0.0.1:8000/admin/
📄 Лицензия
Этот проект распространяется под лицензией MIT.
🤝 Вклад в проект

Форкните репозиторий
Создайте ветку для новой функции (git checkout -b feature/my-feature)
Зафиксируйте изменения (git commit -m 'Add my feature')
Отправьте ветку (git push origin feature/my-feature)
Откройте Pull Request
