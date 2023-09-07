# TEST service

## Описание
Проект представляет собой сервис с тестами на разные темы.
В проекте присутствувет авторизация и регистрация.
Используется СУБД Postgresql.

## Как запустить проект на локальной машине
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:dashutalin/test_service.git
cd test_service
```
Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Выполнить миграции:
```bash
python manage.py migrate
```
Загрузитьо тестовые данные в базу данных:
```bash
python manage.py loaddata initial_data.json
```
Запустить проект:
```bash
python manage.py runserver
