# Django-Eccomerce

Django 3.2 - Django-Eccomerce API

### Technology:

- Django 3.2 [Django](https://www.djangoproject.com/)

- Django REST Framework [DRF](https://www.django-rest-framework.org/)

- Azure Database for MySQL[Azure MySQL](https://azure.microsoft.com/en-us/pricing/details/mysql)

- Djoser [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html)

- JSON Web Token [JWT](https://jwt.io/)

- Celery[Celery](https://docs.celeryq.dev/en/stable/)

- Locust [Locust](https://locust.io/)

- Pytest [Pytest](https://docs.pytest.org/)

- Redis [Redis](https://redis.io/)

## List of endpoints (Please open from browser)

## Auth

| Route             | HTTP Verb                      | Requirement          | Description                      |
| ----------------- | ------------------------------ | -------------------- | -------------------------------- |
| /auth/users       | `POST`                         | None                 | Sign Up new user                 |
| /auth/users/me    | `GET`,`PUT`, `PATCH`, `DELETE` | Already login        | Get account details              |
| /auth/jwt/create  | `POST`                         | Already have account | Login and get token              |
| /auth/jwt/refresh | `POST`                         | JWT refresh token    | Get new acces token when expired |

List all endpoint are here https://djoser.readthedocs.io/

## Products

| Route                           | HTTP Verb                       | Requirement     | Description                                |
| ------------------------------- | ------------------------------- | --------------- | ------------------------------------------ |
| /store/products/                | `GET`                           | None            | List all Products.                         |
| /store/products/                | `POST`                          | Login & IsAdmin | Create a new Product                       |
| /store/products/:id             | `GET`                           | None            | Get a Product details.                     |
| /store/products/:id             | `PUT`, `PATCH`, `DELETE`        | Login & IsAdmin | Update a Product details or delete it.     |
| /store/products/:id/reviews     | `GET`, `POST`                   | None            | Get all reviews or post new reviews        |
| /store/products/:id/reviews/:id | `GET`, `PUT`, `PATCH`, `DELETE` | Login & IsAdmin | Modify review or delete it                 |
| /store/products/:id/images      | `GET`, `POST`                   | None            | Get all images or upload new product image |
| /store/products/:id/images/:id  | `GET`, `PUT`, `PATCH`, `DELETE` | None            | Get image or change product image          |

## Collections

| Route                  | HTTP Verb                | Requirement     | Description                    |
| ---------------------- | ------------------------ | --------------- | ------------------------------ |
| /store/collections/    | `GET`                    | None            | Get all list collections       |
| /store/collections/    | `POST`                   | Login & IsAdmin | Create a new collection        |
| /store/collections/:id | `GET`                    | None            | Get a collection details.      |
| /store/collections/:id | `PUT`, `PATCH`, `DELETE` | Login & IsAdmin | Modify collection or delete it |

## Carts

| Route                      | HTTP Verb                | Requirement | Description                                |
| -------------------------- | ------------------------ | ----------- | ------------------------------------------ |
| /store/carts/              | `POST`                   | None        | Create new shopping cart.                  |
| /store/carts/:id           | `GET`, `DELETE`          | None        | Get details cart or delete it              |
| /store/carts/:id/items     | `GET`, `POST`            | None        | Get Get items or add item in shopping cart |
| /store/carts/:id/items/:id | `GET`, `PATCH`, `DELETE` | None        | Modify or delete item in shopping cart     |

## Customers

| Route             | HTTP Verb     | Requirement     | Description                            |
| ----------------- | ------------- | --------------- | -------------------------------------- |
| /store/customers/ | `GET`, `POST` | Login & IsAdmin | Get list all customers or add details. |

## Orders

| Route             | HTTP Verb     | Requirement     | Description                     |
| ----------------- | ------------- | --------------- | ------------------------------- |
| /store/orders/    | `GET`,`POST`  | Login           | Get order list based on cart id |
| /store/orders/:id | `GET`,`PATCH` | Login & IsAdmin | Update status of order          |

## Installation<a name="installation"></a>

### Running Locally

Make sure you have [Python](https://www.python.org/) and [PIP](https://pip.pypa.io/en/stable/) installed.

1.  Clone or Download the repository

    ```
    $ git clone https://github.com/oktaveko/Django_Eccomerce_Okta.git
    $ cd Django_Eccomerce_Okta
    ```

2.  Install Dependencies

    ```
    $ pip install -r requirements.txt (consider using venv)
    ```

3.  Setting DB

    Change DB setting in storefront\settings\dev according to your database detail
    then migrate it using

    ```
    $ python manage.py migrate
    ```

4.  Run Redis Server

    For Windows user you can get redis in here https://github.com/tporadowski/redis/releases
    or you can use docker, just run

    ```
    $ docker run -d -p 6379:6379 redis
    ```

    If you Linux or Mac user just visit and explore here https://redis.io/

5.  Start the application

    ```
    $ python manage.py runserver
    ```

    Your app should now be running on [127.0.0.1:8000/](http://127.0.0.1:8000/).

# Demo

Root url for live demo on [Heroku](https://django-eccomerce-okta.herokuapp.com/)
Just add endpoints that listed above to access API in your browser
