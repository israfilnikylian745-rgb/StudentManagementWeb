from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, add_student, get_all_students, get_student, update_student, delete_student
import os

app = Flask(__name__)

# 1. SECRET KEY - Muhimu kwa login na flash messages
app.secret_key = 'kaka123secret_student_system'

# 2. USER NA PASSWORD YA KUDUMMY - badilisha hapa
USERNAME = 'admin'
PASSWORD = '1234'

# 3. HII NDIO INATENGENEZA TABLE KIOTOMATIKI RENDER IKIFUNGUKA
with app.app_context():
    init_db()


# ROUTE YA LOGIN
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Username au Password si sahihi', 'danger')
    return render_template('login.html')


# ROUTE YA LOGOUT
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


# ROUTE KUU - ORODHA YA WANAFUNZI
@app.route('/index')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    students = get_all_students()
    return render_template('index.html', students=students)


# KUONGEZA MDAFUNZI
@app.route('/add', methods=['GET', 'POST'])
def add():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        grade = request.form['grade']
        add_student(name, course, grade)
        flash('Mwanafunzi ameongezwa kikamilifu!', 'success')
        return redirect(url_for('index'))
    return render_template('add_student.html')


# KUHARIRI MDAFUNZI
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    student = get_student(id)
    if request.method == 'POST':
        name = request.form['name']
        course = request.form['course']
        grade = request.form['grade']
        update_student(id, name, course, grade)
        flash('Taarifa zimesasishwa!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)


# KUFUTA MDAFUNZI
@app.route('/delete/<int:id>')
def delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    delete_student(id)
    flash('Mwanafunzi amefutwa!', 'warning')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
