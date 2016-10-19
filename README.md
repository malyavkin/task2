# Установка

* Установка зависимостей
    `pip install -r /path/to/requirements.txt`

* Начальная миграция
    `python manage.py makemigrations rest`
    `python manage.py migrate`

* создание суперпользователя
    `python manage.py createsuperuser`

# Запуск и работа
    `python manage.py runserver`
* Создание других пользователей возможно через админку джанго или через его консоль:

    ```
    $> manage.py shell
    >>> from django.contrib.auth.models import User
    >>> user=User.objects.create_user('foo', password='bar')
    >>> user.is_superuser=True
    >>> user.is_staff=True
    >>> user.save()
    ```

* Вызов методов апи:
 * `POST /tasks/`
  Выполняет задачу:
  * Nное простое число. Пример тела запроса:
    ```
    {
        "task_name": "nth_prime",
        "args": "100000"
    }
    ```
  * факторизация числа. Пример тела запроса:
    ```
    {
        "task_name": "factorize",
        "args": "1440"
    }
    ```
  * ping сервера. Пример тела запроса (hostname и число пингов разделяются пробелом):
    ```
    {
        "task_name": "ping",
        "args": "google.com 5"
    }
    ```
 * `get /tasks/`
  Возвращает результаты прошлых задач

