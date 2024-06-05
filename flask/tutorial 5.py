from flask import Flask, redirect, url_for, render_template, request, flash
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = "strong secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trips.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Trips(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    start = db.Column(db.String(100), nullable=False)
    finish = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    comment = db.Column(db.String(100), nullable=True, default="-")

    def __init__(self, name, surname, phone, email, start, finish, date, comment=""):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.start = start
        self.finish = finish
        self.date = date
        self.comment = comment

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField()

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
        if user and form.password.data == user.password_hash:
            print(form.remember.data)
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
    return render_template("admin.html", data=trips)

@app.route("/edit_trip/<int:trip_id>", methods=["GET", "POST"])
def edit_trip(trip_id):
    trip = Trips.query.get(trip_id)
    if request.method == "POST":
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
    return render_template("edit_trip.html", trip=trip)

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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
