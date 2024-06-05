from flask import Flask, redirect, url_for, render_template, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db
from app.models import User, Trips
from app.forms import LoginForm
from datetime import datetime

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login/', methods=['post', 'get'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('admin'))
        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/user")
def user():
    trips = Trips.query.all()
    return render_template("user.html", data=trips)

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        if "edit" in request.form:
            trip_id = request.form["edit"]
            return redirect(url_for("edit_trip", trip_id=trip_id))
        elif "delete" in request.form:
            trip_id = request.form["delete"]
            trip_to_delete = Trips.query.get(trip_id)
            db.session.delete(trip_to_delete)
            db.session.commit()
            return redirect(url_for("admin"))
    trips = Trips.query.all()
    users = User.query.all()
    return render_template("admin.html", trips=trips, users=users)

@app.route("/edit_trip/<int:trip_id>", methods=["GET", "POST"])
@login_required
def edit_trip(trip_id):
    trip = Trips.query.get(trip_id)
    if request.method == "POST":
        try:
            trip.name = request.form["name"]
            trip.surname = request.form["surname"]
            trip.phone = request.form["phone"]
            trip.email = request.form["email"]
            trip.start = request.form["start"]
            trip.finish = request.form["finish"]
            trip.date = datetime.strptime(request.form["date"], '%Y-%m-%d').date()
            trip.comment = request.form["comment"]
            db.session.commit()
            return redirect(url_for("admin"))
        except KeyError as e:
            flash(f"Missing form field: {e}", "error")
            return redirect(url_for("edit_trip", trip_id=trip_id))
    return render_template("edit_trip.html", trip=trip)

@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == "POST":
        try:
            user.name = request.form["name"]
            user.username = request.form["username"]
            user.email = request.form["email"]
            if request.form["password"]:
                user.set_password(request.form["password"])
            db.session.commit()
            return redirect(url_for("admin"))
        except KeyError as e:
            flash(f"Missing form field: {e}", "error")
            return redirect(url_for("edit_user", user_id=user_id))
    return render_template("edit_user.html", user=user)

@app.route("/create_user", methods=["GET", "POST"])

@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        phone = request.form["phone"]
        email = request.form["email"]
        start = request.form["start"]
        finish = request.form["finish"]
        date = datetime.strptime(request.form["date"], '%Y-%m-%d').date()
        comment = request.form["comment"]
        new_trip = Trips(name, surname, phone, email, start, finish, date, comment)
        db.session.add(new_trip)
        db.session.commit()
        return redirect(url_for("user"))
    return render_template("create_user.html")

@app.route("/create_admin", methods=["GET", "POST"])
@login_required
def create_admin():
    if not current_user.is_admin:
        flash("You do not have access to this page.", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        try:
            name = request.form["name"]
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]
            user = User(name=name, username=username, email=email)
            user.set_password(password)
            user.is_admin = True
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("admin"))
        except KeyError as e:
            flash(f"Missing form field: {e}", "error")
            return redirect(url_for("create_admin"))
    return render_template("create_admin.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("home"))
