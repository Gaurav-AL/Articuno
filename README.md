# Articuno Assignment Non Bonus Part

1) Tables are created using SQL command, executed through import psycopg2 execute()
2) Using POSTGRESQL database on localhost
3) created under vitrual environment
$) Table Querying is also done using SQL command

# Usage

1) clone this repository into your system
2) activate the virtual environment through ##source /bin/activate
3) run -> pip -r install requirements.txt
4) run -> export DB_USERNAME="{your_postgres_username}"
5) run -> export DB_PASSWORD="{your_postgres_password}"
4) run -> python app.py

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




