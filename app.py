
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///response.db")

# Make sure API key is set

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    data = db.execute("SELECT 10.0*AVG(diff) as percentage, week FROM remarks GROUP BY week")
    if not data:
        return apology("we're no strangers to no response")
    return render_template("index.html", datas = data)


@app.route("/response", methods=["GET", "POST"])
@login_required
def response():
    """Validate and store the response"""
    if request.method == "GET":
        return render_template("./response.html")

    text = request.form.get("text")
    week = request.form.get("week")
    diff = request.form.get("diff")
    id = session["user_id"]

    if not text or not week or not diff:
        return apology("Never Gonna Give all fields")

    week = int(week)
    diff = int(diff)

    if week < 0 or week > 9:
        return apology("Never Gonna Give Valid Week")
    if diff < 1 or diff > 10:
        return apology("Never Gonna Give Valid Difficulty")
    db.execute("INSERT INTO remarks (user_id, msg, diff, week) VALUES(?,?,?,?)", id, text, diff, week)

    return redirect("/")


@app.route("/week0")
@login_required
def week0():
    """Show comments and remarks for the following week"""

    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 0")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)


@app.route("/week1")
@login_required
def week1():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 1")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week2")
@login_required
def week2():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 2")
    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week3")
@login_required
def week3():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 3")
    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week4")
@login_required
def week4():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 4")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week5")
@login_required
def week5():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 5")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week6")
@login_required
def week6():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 6")
    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week7")
@login_required
def week7():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 7")
    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week8")
@login_required
def week8():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 8")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)

@app.route("/week9")
@login_required
def week9():
    """Show comments and remarks for the following week"""
    data = db.execute("SELECT * FROM remarks JOIN users ON users.id = remarks.user_id WHERE week = 9")

    if not data:
        return apology("Never Gonna Give Response")

    return render_template("discuss.html", datas=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Never Gonna Give full fields", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Never Gonna Give full fields", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():
    """Change User password"""
    if request.method == "GET":
        return render_template("reset.html")
    id = session["user_id"]
    psw = request.form.get("pass")
    cpsw = request.form.get("confirm")

    if not psw or not cpsw:
        return apology("Never Gonna Give full fields", 403)

    if not psw == cpsw:
        return apology("Never Gonna Give right confirmation", 403)

    hash = generate_password_hash(psw)
    db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, id)

    session.clear()
    flash("Changed")
    return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        user = request.form.get("username")
        psw = request.form.get("password")
        cpsw = request.form.get("confirmation")

        if not user or not psw or not cpsw:
            return apology("Never Gonna Give full fields", 400)

        if not psw == cpsw:
            return apology("Never Gonna Give right confirmation", 400)

        if db.execute("SELECT username FROM users WHERE username = ?", user):
            return apology("Never Gonna Let you have this Username", 400)

        psw = generate_password_hash(psw)
        register = db.execute("INSERT INTO users (username, hash) VALUES(?,?)", user, psw)
        session["user_id"] = register

        return redirect("/")

    return render_template("register.html")
