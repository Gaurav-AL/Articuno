from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import warnings
from flask_migrate import Migrate, migrate
from init_db import cur,conn
warnings.filterwarnings(action='ignore',module='.*paramiko.*')


# creating flask object name app
app = Flask(__name__)

# user_increment,msg_increment = 0,0
# # create db
# # adding configuration for using a postgresql database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gaurav:gaurav@127.0.0.1:5432/mydb'
 
# # Creating an SQLAlchemy instance
# db = SQLAlchemy(app)

# migrate = Migrate(app, db)
# # Settings for migrations
# migrate = Migrate(app, db)


# creating routes
@app.route('/')
def hello():
    return {
        "messgae":"Let's Start testing"
    }
    
@app.route('/createuser',methods = ['POST'])
def create_user():
    data = request.json
    name = data['name']
    age = data['age']
    
    cur.execute("INSERT INTO users(name,age) VALUES (%s, %s) RETURNING id", (name, age))
    fetched_id = cur.fetchone()[0]
    
    conn.commit()
    return {
        "status_code":200,
        "message":"User created with id "+ str(fetched_id)
    }

'''
This routes means user with username have posted message with post details(message_id,message_desc,message_title)
'''
@app.route('/postmessage/<username>',methods =['POST'])
def postmessage(username):
    data = request.json
    message = data['msg']
    query = 'INSERT INTO message(msg_dsc,name) VALUES (%s,%s) RETURNING msg_id'
    cur.execute(query , (message,username))
    fetched_id = cur.fetchone()[0]
    conn.commit()
    return {
        "status_code":200,
        "message": "Successfully committed your message with message_id "+ str(fetched_id)
    }

'''
This routes means view message of user username
'''
@app.route('/viewmessage/<username>',methods = ['GET'])
def getMessages(username):
    cur.execute('SELECT name from users WHERE name = %(name)s',{"name":username})
    if(not cur.fetchone()):
        return {"status_code":200,
                "message":"User doesn't exist, first post message with this username"
                }
    #fetching all messages in ascending order of msg_id
    query = 'SELECT date_added,msg_dsc from message WHERE name = %(name)s ORDER BY msg_id'
    cur.execute(query,{"name":username})
    all_message = cur.fetchall()
    if(len(all_message) == 0):
        return {
            "status_code":200,
            "message":"Either no rows added"
        }
    res = []
    #creating list of dcitionary 
    for index,msg in enumerate(all_message):
        res.append({"Date":msg[0],"message":msg[1]})
    return res


'''
This routes means add likes in message of user username and having message_id 
'''
@app.route('/addlikes/<username>/<int:message_id>', methods=['GET'])
def addlikeforMessages(username,message_id):
    query = 'INSERT INTO addlikes(msg_id,name) VALUES(%s,%s) RETURNING msg_id'
    cur.execute(query,(message_id,username))
    fetched_id = cur.fetchone()[0]
    conn.commit()
    
    # checking if there is a user message in message table
    cur.execute("SELECT * from message")
    if(not cur.fetchall()):
        return{
            "message":"NO RECORDS IN message TABLE"
        }
    
    
    return {
        "status_code":200,
        "message":"Successfully Updated message id " + str(fetched_id)
    }

'''
This routes means remove likes from message of user username and having message_id 
'''
@app.route('/remlikes/<username>/<int:message_id>', methods=['GET'])
def removelikeforMessage(username,message_id):
    query = 'INSERT INTO remlikes(msg_id,name) values(%s,%s) RETURNING msg_id'
    cur.execute(query,(message_id,username))
    fetched_id = cur.fetchone()[0]
    conn.commit()
    
    # checking if there is a user message in message table
    cur.execute("SELECT * from message")
    if(not cur.fetchall()):
        return{
            "message":"NO RECORDS IN message TABLE"
        }
    
    return {
        "status_code":200,
        "message":"Successfully Updated message id " + str(fetched_id)
    }


'''
This routes means show likes of user username with message_id 
'''
@app.route('/viewlikes/<username>/<message_id>', methods=['GET'])
def viewLikes(username,message_id):
    #fetching likes count from database
    query = 'SELECT likes_count from message WHERE name = %s AND msg_id = %s'
    cur.execute(query,(username,message_id))
    
    res = cur.fetchone()
    if(not res):
        return {"status_code":200,"total_likes":0}
    
    return {"username":username,"message_id":message_id,"total_likes":res[0]}

#starting server
if __name__== "__main__":
    app.run(debug=True) 
    
    
    
