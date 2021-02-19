# How to run this project
- Build the image:
``` docker-compose build ```
- Run the image:
``` docker-compose up -d ```
- Build the superUser for the MySQL database
``` docker exec -it longroad_db_1 /bin/bash ```
Run inside of the container to create the django superuser:
``` python3 manage.py createsuperuser ```
Watch it run by navigating to: ```localhost``` on your browser