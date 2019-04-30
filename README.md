# Django Sandbox

Install Django, create site project and run development server.
> pip install django

> python -m django --version

Create django project. Project can contain config and many web apps.
Particular web app can belong to many projects.
> django-admin startproject SiteSandbox

Run **development** server for a project.
> python manage.py runserver

Deployment of Python based web applications on web servers relies on WSGI standard.

Create web application named polls in SiteSandbox project.
> python manage.py startapp polls

After implementation the web app page is http://localhost:8000/polls/ .

To initialize database defined in settings.py with tables for INSTALLED_APPS.
> python manage.py migrate

To update database for polls app after schema change
create migration files
> python manage.py makemigrations polls

and create sql statements
> python manage.py sqlmigrate polls 0001

and check correctness
> python manage.py check

and update db
> python manage.py migrate

To manipulate model and save changes in db
> python manage.py shell

Create admin for project (grzesk grzesiek)
> python manage.py createsuperuser
