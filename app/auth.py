from flask import Blueprint, render_template, redirect, request, url_for, flash
from .models import User
from . import db, bcrypt
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login Successful 🚀")
            return redirect(url_for('main.dashboard'))
        else:
            flash("Invalid username or password")

    return render_template("login.html")


@auth.route("/register", methods=['POST'])
def register():

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Fill all fields")
        return redirect(url_for('auth.login'))

    existing = User.query.filter_by(username=username).first()
    if existing:
        flash("Username already exists")
        return redirect(url_for('auth.login'))

    hashed = bcrypt.generate_password_hash(password).decode('utf-8')

    role = "owner" if username == "vivek" else "trainee"

    user = User(username=username, password=hashed, role=role)

    db.session.add(user)
    db.session.commit()

    flash("Account created")
    return redirect(url_for('auth.login'))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))