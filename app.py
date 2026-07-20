from flask import Flask, render_template, request, redirect, session, flash
from functions import get_all_students, add_student, search_students, get_student_by_id, update_student, delete_student, create_user, check_user

app = Flask(__name__)
app.secret_key = "mysecretkey123" # Badili hii iwe ngumu zaidi baadae

# HII NI DECORATOR YA KUZUIA MTU ASIYE NA LOGIN
def login_required(f):
    def wrap(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/login")
    wrap.__name__ = f.__name__
    return wrap

# ROUTE YA REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if create_user(username, password):
            flash("Account created successfully! Please login.")
            return redirect("/login")
        else:
            flash("Username already exists!")
    return render_template("register.html")

# ROUTE YA LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = check_user(username, password)
        if user:
            session["user"] = username
            return redirect("/")
        else:
            flash("Invalid username or password!")
    return render_template("login.html")

# ROUTE YA LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# HOME PAGE - ORODHA YA WANAFUNZI
@app.route("/")
@login_required
def home():
    keyword = request.args.get("search")
    if keyword:
        students = search_students(keyword)
    else:
        students = get_all_students()
    return render_template("index.html", students=students, username=session["user"])

# ROUTE YA KUONGEZA MWANAFUNZI
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        add_student(name, age)
        return redirect("/")
    return render_template("add_student.html")

# ROUTE YA KUHARIRI MWANAFUNZI
@app.route("/edit/<int:student_id>", methods=["GET", "POST"])
@login_required
def edit(student_id):
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        update_student(student_id, name, age)
        return redirect("/")
    
    student = get_student_by_id(student_id)
    return render_template("edit_student.html", student=student)

# ROUTE YA KUFUTA MWANAFUNZI
@app.route("/delete/<int:student_id>")
@login_required
def delete(student_id):
    delete_student(student_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True) 