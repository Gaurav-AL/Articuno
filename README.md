# Articuno Assignment Non Bonus Part

1) Tables are created using SQL command, executed through import psycopg2 execute()
2) Using POSTGRESQL database on localhost
3) created under vitrual environment
$) Table Querying is also done using SQL command

# Usage

1) clone this repository into your system
2) create virtual environment using -> python3 -m venv {virtual_environment name}
3) activate your virtual environment source /bin/activate
4) run -> pip -r install requirements.txt
5) run -> export DB_USERNAME="{your_postgres_username}"
6) run -> export DB_PASSWORD="{your_postgres_password}"
7) run -> python app.py

# Endpoints 

### hello message
## 1) http://127.0.0.1:5000

### create users
## 2) http://127.0.0.1:5000/createuser

### post message by user by username
## 3) http://127.0.0.1:5000/postmessage/<username>

### view message posted by user by username
## 4) http://127.0.0.1:5000/viewmessage/<username>

### Add likes to message having message_id and user as username
## 5) lhttp://127.0.0.1:5000/addlikes/<username>/<int:message_id>

### Remove like from message having message_id and user as username
## 6) http://127.0.0.1:5000/remlikes/<username>/<int:message_id>

### View likes
## 7) http://127.0.0.1:5000/viewlikes/<username>/<message_id>

# Database Triggers
There are total of 3 triggers 

# Database Tables
Thera are total of three tables namely users, message, likes


# Articuno bonus Part setup docker db

1) install docker-desktop in your machine - (for window install windows version and for linux/Mac download particular versions)
2) Once Installed run "docker compose up" where your docker-compose.yml file locates and pgadmin and postgres images will be pulled from docker hub.
3) Check 127.0.0.1:5432 on browser for postgresql and 127.0.0.1:5050 for pgadmin





