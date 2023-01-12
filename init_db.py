import os
import psycopg2

#creatinf database connection
conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
#User table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'name varchar (150) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

#Message table
cur.execute('DROP TABLE IF EXISTS message;')
cur.execute('CREATE TABLE message ( msg_id serial PRIMARY KEY,'
                                    'msg_dsc varchar (255) NOT NULL,'
                                    'name varchar (150) NOT NULL,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                    'likes_count integer DEFAULT 0);')
# AddLike table
cur.execute('DROP TABLE IF EXISTS addlikes;')
cur.execute('CREATE TABLE addlikes( msg_id integer NOT NULL,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP,'
                                    'name varchar (255) NOT NULL);')
# REMOVE Like table
cur.execute('DROP TABLE IF EXISTS remlikes;')
cur.execute('CREATE TABLE remlikes( msg_id integer NOT NULL,'
                                    'date_removed date DEFAULT CURRENT_TIMESTAMP,'
                                    'name varchar (255) NOT NULL);')

#creating trigger after insert in table message
cur.execute('DROP TRIGGER IF EXISTS user_insertion ON message;')
cur.execute('DROP FUNCTION IF EXISTS userinsertion();')

cur.execute('CREATE FUNCTION userinsertion() RETURNS TRIGGER AS $user_insert$ ' 
            'BEGIN '
            'INSERT INTO users(name,date_added) values(new.name,new.date_added);'
            'RETURN NEW;'
            'END;'
            '$user_insert$ LANGUAGE plpgsql;')

#triggering message insert message
cur.execute('CREATE TRIGGER user_insertion AFTER INSERT ON message '
            'FOR EACH ROW EXECUTE PROCEDURE userinsertion();')

#creating trigger after insertion on addlikes in table likes
cur.execute('DROP TRIGGER IF EXISTS likes_added ON addlikes;')
cur.execute('DROP FUNCTION IF EXISTS likesadded();')

cur.execute('CREATE FUNCTION likesadded() RETURNS TRIGGER AS $like_add$ ' 
            'BEGIN '
            'UPDATE message SET likes_count=likes_count + 1 WHERE msg_id = new.msg_id;'
            'RETURN NEW;'
            'END;'
            '$like_add$ LANGUAGE plpgsql;')

#triggering likesadded() function
cur.execute('CREATE TRIGGER likes_added AFTER INSERT ON addlikes '
            'FOR EACH ROW EXECUTE PROCEDURE likesadded();')


#creating trigger after deletion on remlikes in table likes
cur.execute('DROP TRIGGER IF EXISTS likes_removed ON remlikes;')
cur.execute('DROP FUNCTION IF EXISTS likesremoved();')

cur.execute('CREATE FUNCTION likesremoved() RETURNS TRIGGER AS $like_rem$ '
            'BEGIN '
            'UPDATE message SET likes_count=likes_count-1 WHERE msg_id = new.msg_id;'
            'RETURN NEW;'
            'END;'
            '$like_rem$ LANGUAGE plpgsql;')

#triggering likesremoved() function
cur.execute('CREATE TRIGGER likes_removed AFTER INSERT ON remlikes '
            'FOR EACH ROW EXECUTE PROCEDURE likesremoved();')


#commiting into database                            
conn.commit()
