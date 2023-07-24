from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://////home/vurudi100/Downloads/Flask Exercise 2- Sign up/database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        # Validate user's credentials against the database
        user = User.query.filter_by(username=uname, password=passw).first()
        if user:
            return redirect(url_for("secret_page"))
        else:
            error = "Invalid username or password."

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fname = request.form['firstname']
        lname = request.form['lastname']
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        confirm_passw = request.form['confirm_password']

        # Password matching and criteria validation
        if passw != confirm_passw:
            error = "Passwords do not match."
            return render_template("register.html", error=error)

        if len(passw) < 8:
            error = "Password must be at least 8 characters long."
            return render_template("register.html", error=error)

        # Check if the username already exists in the database
        existing_username = User.query.filter_by(username=uname).first()
        if existing_username:
            error = "Username already exists."
            return render_template("register.html", error=error)

        # Check if the email already exists in the database
        existing_email = User.query.filter_by(email=mail).first()
        if existing_email:
            error = "Email address already exists."
            return render_template("register.html", error=error)

        # All validations passed, create a new user record
        new_user = User(first_name=fname, last_name=lname, username=uname, email=mail, password=passw)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the thank you page after successful registration
        return redirect(url_for("thankyou"))

    return render_template("register.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/secretPage")
def secret_page():
    return render_template("secretPage.html")

if __name__ == "__main__":
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()

    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
