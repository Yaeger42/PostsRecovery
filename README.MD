Important commands to run the docker compose:
``` $ docker-compose up ```
In another separate tab:
``` $ docker-compose run --rm web python manage.py createsuperuser ```
This is important to run in order to create the superuser in the MYSQL Database