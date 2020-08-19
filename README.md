# NMAP Scanner

Starting the server

> conda activate siteenv
> python manage.py runserver

Starting redis-server

> redis-server

Starting celery worker

> celery worker -A scanner --log-level=info

