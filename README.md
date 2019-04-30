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
