import sqlite3

def init_db():
    conn = sqlite3.connect('somo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    
    # Tumebadilisha hapa: tumeongeza Age
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY, name TEXT, course TEXT, grade TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

def get_students():
    conn = sqlite3.connect('somo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    conn.close()
    return students

def add_student(name, course, grade, age):
    conn = sqlite3.connect('somo.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, course, grade, age) VALUES (?,?,?,?)", (name, course, grade, age))
    conn.commit()
    conn.close()

def update_student(id, name, course, grade, age):
    conn = sqlite3.connect('somo.db')
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, course=?, grade=?, age=? WHERE id=?", (name, course, grade, age, id))
    conn.commit()
    conn.close()

def delete_student(id):
    conn = sqlite3.connect('somo.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close().close()
