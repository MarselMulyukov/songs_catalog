## API Каталог исполнителей и их альбомов с песнями


## Возможности сервиса:
документация API по адресу /api/v1/swagger/
список альбомов
список исполнителей
страницы с содержимым альбома
страницы с альбомами исполнителя
административная панель с возможностью добавления, удаления, редактирования сущностей

## Проект готов для запуска на локальной машине:
1. Склонировать репозиторий git clone https://github.com/MarselMulyukov/songs_catalog.git
2. Перейти в директорию с инфраструктурой cd songs_catalog/infra
3. Создать .env файл с переменными окружения по примеру example_env
4. Выполнить команду docker-compose -d --build
5. Выполнить команду docker-compose exec backend python manage.py migrate
6. Выполнить команду docker-compose exec backend python manage.py collectstatic
8. Проект должен быть доступен по адресу 127.0.0.1/api/v1/
9. Админка должна быть доступна по адресу 127.0.0.1/admin/

## Технологии и требования
Python 3.6+
Django 2.2.19
Django REST Framework 3.13
Docker Compose

## Автор: Мулюков Марсель