![foodgram-project-workflow](https://github.com/inood/foodgram-project/workflows/foodgram-project-workflow/badge.svg)

### «Продуктовый помощник».
Это онлайн-сервис, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

Демо: http://188.225.78.124/

### Установка

1. Подготовка

    Приложение работает за счет [Docker](https://docs.docker.com/engine/install/) и [docker-compose](https://docs.docker.com/compose/install/)
    
    Установка для разных операционных систем описана в инструкциях по ссылкам выше

2. Запуск сервиса
    
    Приложение работает в двух docker контейнерах, для сборки и запуска всего окружения необходимо выполнить комманду
 
    ```
    docker-compose up
   ```
    
### Первоначальная настройка

1. Предварительная миграция (создание таблиц в БД)

    ```
    docker-compose run web python manage.py migrate
    ```

2. Создание суперпользователя
    ```
   docker-compose run web python manage.py createsuperuser
   ```
3. Загрузка демонстрационных данных
    ```
   docker-compose run web python manage.py loaddata fixtures.json
   ```



### Используемый стек
* [Python](https://www.python.org/) 
* [Django](https://www.djangoproject.com/) 
* [Django-restframework](https://www.django-rest-framework.org/)
* [Docker](https://www.docker.com/)
* [Docker-compose](https://docs.docker.com/compose/)
* [Postgresql](https://www.postgresql.org/)


### Автор
Морозов Дмитрий <inood@yandex.ru>
данный проект создан в рамках обучения на курсах Yandex-Praktikum 
