
# auth.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from models import User

auth = Blueprint("auth", __name__)


# ==================================================
# REGISTER
# ==================================================
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        college = request.form.get("college")
        department = request.form.get("department")
        password = request.form.get("password")

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("auth.register"))

        # Hash password
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = User(
            name=name,
            email=email,
            phone=phone,
            college=college,
            department=department,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please login.")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# ==================================================
# LOGIN
# ==================================================
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.name
            session["user_email"] = user.email

            flash("Login successful.")
            return redirect(url_for("dashboard.dashboard_home"))

        flash("Invalid email or password.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


# ==================================================
# LOGOUT
# ==================================================
@auth.route("/logout")
def logout():

    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("home"))


# ==================================================
# CHECK LOGIN
# ==================================================
def is_logged_in():
    return "user_id" in session


# ==================================================
# GET CURRENT USER
# ==================================================
def current_user():
    if "user_id" in session:
        return User.query.get(session["user_id"])
    return None

