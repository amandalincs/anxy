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

def get_all_cat():
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM categories")
    
    cur.execute(get_stmt)
    categories = cur.fetchall()

    cur.close()
    con.close()
    return categories

def get_cat(cat_id):
    con, cur = db_connect()
    get_stmt = ("SELECT * FROM categories "
                "WHERE c_id=(%s)")
    
    cur.execute(get_stmt,(cat_id,))
    category = cur.fetchall()

    cur.close()
    con.close()

    return category

def create_cat(name):
    con, cur = db_connect()
    insert_stmt = ("INSERT INTO categories(category) "
                "VALUES (%s)")
    
    cur.execute(insert_stmt, (name,))
    con.commit()

    db_close(con,cur)
    return 

def edit_cat(cat_id, name):
    con, cur = db_connect()
    update_stmt = ("UPDATE categories "
                    "SET category = (%s) "
                    "WHERE c_id = (%s)")
    
    cur.execute(update_stmt, (name,cat_id))
    con.commit()

    db_close(con,cur)

def delete_cat(cat_id):
    con, cur = db_connect()
    delete_stmt =  ("DELETE FROM categories "
                    "WHERE c_id = (%s)")
    
    cur.execute(delete_stmt, (cat_id,))
    con.commit()

    db_close(con,cur)
    






def create_course(name,instr,letter,sign,quarter,year,thoughts):
    """
    course_data: tuple
    """

    con = db_connect()
    cur = con.cursor()
    insert_stmt = ("INSERT INTO courses (name, instructor, letter_grade, sign_grade, quarter, year, thoughts) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)")

    cur.execute(insert_stmt,(name,instr,letter,sign,quarter,year,thoughts))
    con.commit()

    cur.close()
    con.close()

def get_courses():
    con = db_connect()
    cur = con.cursor()
    get_stmt = ("SELECT * FROM courses")
    
    cur.execute(get_stmt)
    courses = cur.fetchall()

    cur.close()
    con.close()
    return courses

def get_single_course(course_id):
    con = db_connect()
    cur = con.cursor()
    get_stmt = ("SELECT * FROM courses "
                "WHERE course_id=(%s)")
    
    cur.execute(get_stmt,(course_id,))
    course = cur.fetchone()

    cur.close()
    con.close()
    return course
    

def delete_single_course(course_id):
    con = db_connect()
    cur = con.cursor()

    delete_stmt = ("DELETE FROM courses "
                    "WHERE course_id = (%s)")
    
    cur.execute(delete_stmt,(course_id,))
    con.commit()

    cur.close()
    con.close()

def delete_all_courses():
    con = db_connect()
    cur = con.cursor()

    all_courses = get_courses()

    delete_stmt = ("DELETE FROM courses "
                    "WHERE name = (%s)")
    for _, course in all_courses:
        cur.execute(delete_stmt,(course,))
        con.commit()

    cur.close()
    con.close()

def update_course(course_id,name,instr,letter,sign,quarter,year,thoughts):
    con = db_connect()
    cur = con.cursor()

    all_courses = get_courses()

    update_stmt = ("UPDATE courses "
                    " SET name = %s, instructor = %s, letter_grade = %s, sign_grade = %s, quarter = %s, year = %s, thoughts = %s "
                    " WHERE course_id = %s")
    
    cur.execute(update_stmt,(name,instr,letter,sign,quarter,year,thoughts,course_id))
    con.commit()

    cur.close()
    con.close()