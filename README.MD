# How to run this project
- After copying the project, in the root folder create an archive called MySQL.env
- Generate a secret key (you can use any method)
- Inside of ```MySQL.env``` enter these keys:```
        SECRET_KEY=YourGeneratedSecretKeyHere                   
        MYSQL_ROOT_PASSWORD=yourPassword
        MYSQL_PASSWORD=yourPassword 
        ```
- Build the image:
``` docker-compose build ```
- Run the image:
``` docker-compose up -d ```
- Build the django super user for the MySQL database
``` docker exec -it longroad_db_1 /bin/bash ```
- Run inside of the container to create the django superuser:
``` python3 manage.py createsuperuser ```
Watch it run by navigating to: ```localhost``` on your browser