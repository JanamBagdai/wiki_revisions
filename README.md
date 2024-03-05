# django-base setup
A basic boilerplate Django project prepped with poetry and Rollup. It uses the Django project default database SQLite.

## Setup

For history's sake, this setup was based off of the instructions here: https://builtwithdjango.com/blog/basic-django-setup.

1. Install [poetry](https://python-poetry.org/docs/#installation). This allows us to run our project in a virtual environment and will handle the installation of Django and other python libraries.

2. Run `poetry install` to install dependencies.

3. Rename `myproject` to whatever you'd like your project to be named. You will want to change the name in `pyproject.toml`, the Django project directory name `myproject/`, `manage.py`, and `settings.py`.

4. Change `TIME_ZONE` in `settings.py` to your timezone.

5. Run `poetry run python manage.py migrate` to initialize your local database.

6. Create a superuser for your local Django instance. Run `poetry run python manage.py createsuperuser`. Be sure to save your username and password in a responsible location.

7. Install [node](https://nodejs.org/en).

8. Run `npm install`.

9. Run `npm run build`.

## Running the server

Run `poetry run python manage.py runserver`.


## Running other Django commands

See Django documentation for other commands, such as generating and applying migrations. Commands can be used as normal, preceded by `poetry run`. For example, see "Running the server" above.

## Running tests

To run python tests, use `poetry run pytest`.
To run TS/JS tests, use `npm run test`.

# output
URL: http://127.0.0.1:8000/pages/
The user is required to enter a numerical value that will serve as the window width. For instance, if an event occurs on date 'X,' then considering the number entered (let's call it 'N'), the system will look for revisions within the time frame from 'X' to 'X + N' days for that particular event.

![image](https://github.com/JanamBagdai/wiki_revisions/assets/58061119/4a2112b4-83e9-404a-9066-e7c884b46d58)


![image](https://github.com/JanamBagdai/wiki_revisions/assets/58061119/4a9d4b30-40a2-4ade-9f1b-010935c70bfe)

![image](https://github.com/JanamBagdai/wiki_revisions/assets/58061119/a199d6fa-81b2-458c-9f15-111cc7d479eb)


