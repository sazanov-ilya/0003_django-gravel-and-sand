http://127.0.0.1:8000/
http://127.0.0.1:8000/admin
admin - admin

http://127.0.0.1:8000/get_all_products/?format=json
http://127.0.0.1:8000/get_all_products


В консоли PyCharm

===================
Начальные настройки
===================

Устанавливаем jango
pip install jango

---
Создать и запустить проект
django-admin startproject gravel_and_sand

---
Переход в корневой каталог проекта
cd gravel_and_sand

---
Создаем (запускаем) приложение
python manage.py startapp app_first__gravel_and_sand

И прописываем его в INSTALLED_APPS

---
? Пользователь для подключения к БД
createuser gravel_and_sand_user

---
Запуск сервера
python manage.py runserver

Чтобы остановить runserver жмем ctrl + C


Добавляем расширение для PostgreSQL
psycopg2
pip install psycopg2


===
Настройка БД
===
1
CREATE DATABASE gravel_and_sand;
2
CREATE USER gravel_and_sand_user WITH PASSWORD 'Version2';
Дополнительно для юниттестов даем права на создание БД
3
ALTER ROLE gravel_and_sand_user  SET client_encoding TO 'utf8';
ALTER ROLE gravel_and_sand_user  SET default_transaction_isolation TO 'read committed';
ALTER ROLE gravel_and_sand_user  SET timezone TO 'UTC';
4
GRANT ALL PRIVILEGES ON DATABASE gravel_and_sand TO gravel_and_sand_user;
5
проверка подключения в консоли
python manage.py migrate
6
запуск сервера
python manage.py runserver
Чтобы остановить runserver жмем shift + ctrl + C

8
создаем модель (таблицу)
для применения
python manage.py makemigrations app_first__gravel_and_sand
и потом
python manage.py migrate

---
работа с БД
---
Для просмотра данных таблиц БД можнго использовать специальный модуль
запускаем
python manage.py shell
выход из консоли shell
quit()

Заходим в таблицу
from app_first__gravel_and_sand.models import Products

Добавляем данные
Products.objects.create(product_name='Песок', product_unit='тонна', product_price='3000', product_description='Песок как песок')
Products.objects.create(product_name='Щебень', product_unit='тонна', product_price='4000', product_description='Щебень обычный')


=======
Админка
=======
python manage.py runserver

---
создание суперпользователя для проекта jango
python manage.py createsuperuser
admin - admin

---
добавление моделей в админку
...


=====================
django rest framework (установка )
=====================
Учтанавливаем расширение djangorestframework

в папке приложения app_first__gravel_and_sand
создаем serializers.py
создаем класс GravelAndSandSerializer

создаем view.py

через urls.py пообрасываем запрос из view.py

---
1.
Селеризатор строится по модели
Может быть несколько отдельных селеризаторов на одну модель? 
Или всегда если модель одна, то только через наследование?

2.
Вью строится по селеризатору
Может быть несколько вью на один селеризатор?

3
прописываем вью в урлс


==========
юнит тесты
==========

В каталоге приложения удаляем файл tests.py
И создаем новый каталог (python package) tests
В каталоге создаем файл 
test_logic

В котором прописываем класс с проверкой функционала всех процедур

from unittest import TestCase
from app_first__gravel_and_sand.logic import operations
class LogicTastCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)
	...


Запуск тестов в консоли
python manage.py test app_first__gravel_and_sand.tests

запуск всех тестов
python manage.py test .

---
тест api
test_api.py
тест serializer(а)
test_serializers.py

python manage.py test app_first__gravel_and_sand.tests.test_api
python manage.py test app_first__gravel_and_sand.tests.test_serializers

---
пакет для тестов
проверка на сколько тесты все проверяют
coverage

coverage run --source='.' python manage.py test .

python manage.py test .
coverage run manage.py test .
coverage report
coverage html


--
superadmin для БД проекта
пользователю gravel_and_sand_user
даем права на создание БД

---
подключение к бд в консоли
...
createuser -s -P superadmin

