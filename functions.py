from database import get_connection

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return students

def add_student(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def search_students(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE name LIKE ?", ('%' + keyword + '%',))
    students = cursor.fetchall()
    conn.close()
    return students

# NEW: Get one student by ID
def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

# NEW: Update student
def update_student(student_id, name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Students SET name = ?, age = ? WHERE id = ?", (name, age, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()      

#NEW: User functions
def create_user(username,password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username,password) VALUES(?,?)",(username,password))
        conn.commit()
        return True
    except:
        return False #Username tayari ipo.
    finally:
        conn.close()

def check_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username =? AND password =?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user            