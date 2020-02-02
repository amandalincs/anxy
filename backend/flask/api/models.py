import mysql.connector as mysql

def db_connect_prod():
    con = mysql.connect(
        host = "flask",
        port = "3306",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()
    return con, cur

def db_connect():
    con = mysql.connect(
        host = "127.0.0.1",
        port = "3308",
        user = "root",
        password = "password",
        database = "dbtest"
    )
    cur = con.cursor()
    return con, cur

def db_close(con, cur):
    cur.close()
    con.close()

##### categories #####

def db_get_all_cat():
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM categories")
    
    cur.execute(get_stmt)
    categories = cur.fetchall()

    db_close(con, cur)
    return categories

def db_get_cat(cat_id):
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM categories "
                "WHERE c_id=(%s)")
    
    cur.execute(get_stmt,(cat_id,))
    category = cur.fetchall()

    db_close(con, cur)

    return category

def db_create_cat(name):
    con, cur = db_connect()
    insert_stmt = ("INSERT INTO categories(category) "
                "VALUES (%s)")
    
    cur.execute(insert_stmt, (name,))
    con.commit()

    db_close(con,cur)

def db_edit_cat(cat_id, name):
    con, cur = db_connect()
    update_stmt = ("UPDATE categories "
                    "SET category = (%s) "
                    "WHERE c_id = (%s)")
    
    cur.execute(update_stmt, (name,cat_id))
    con.commit()

    db_close(con,cur)

def db_delete_cat(cat_id):
    con, cur = db_connect()
    delete_stmt = ("DELETE FROM categories "
                    "WHERE c_id = (%s)")
    
    cur.execute(delete_stmt, (cat_id,))
    con.commit()

    db_close(con,cur)
    
##### posts #####
def db_get_all_posts():
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM posts")

    cur.execute(get_stmt)
    posts = cur.fetchall()

    db_close(con, cur)
    return posts

def db_get_post(post_id):
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM posts "
                "WHERE p_id = (%s)")
    
    cur.execute(get_stmt,(post_id,))
    post = cur.fetchall()

    db_close(con, cur)
    return post

def db_create_post(bothering, c_id, goal):
    con, cur = db_connect()
    insert_stmt = ("INSERT INTO posts(Date, bothering, c_id, goal, done) "
                    "VALUES(CURDATE(), (%s), (%s), (%s), false)")
    
    cur.execute(insert_stmt, (bothering,c_id,goal))
    con.commit()

    db_close(con, cur)

def db_edit_post(p_id, bothering, c_id, goal, done):
    con, cur = db_connect()
    update_stmt = ("UPDATE posts "
                    "SET bothering=(%s), c_id=(%s), goal=(%s), done=(%s) "
                    "WHERE p_id=(%s)")
    
    cur.execute(update_stmt, (bothering,c_id,goal,done,p_id))
    con.commit()

    db_close(con, cur)

def db_delete_post(p_id):
    con, cur = db_connect()
    delete_stmt = ("DELETE FROM posts "
                    "WHERE p_id = (%s)")
    
    cur.execute(delete_stmt, (p_id,))
    con.commit()

    db_close(con, cur)
