import sqlite3

import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
from pathlib import Path

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


##Line below only required once, when creating DB.
my_file = Path("/path/to/file")
if not my_file.is_file():
    db.create_all()

# class Register_post_form(FlaskForm):
#     email = StringField("email", validators=[DataRequired()])
#     password = StringField("password", validators=[DataRequired()])
#     name = StringField("Your Name", validators=[DataRequired()])
#     submit = SubmitField("Submit Post")

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    # form = Register_post_form
    if request.method == "POST":
        temp_pw = request.form["password"]
        hash_password = werkzeug.security.generate_password_hash(temp_pw, method='pbkdf2:sha256')
        new_user = User(
            name=request.form["name"],
            email=request.form["email"],
            password=hash_password
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except sqlite3.IntegrityError:
            print("email already registered")
            return redirect(url_for("secrets"))
        except sqlite3.Error:
            print("email already registered")
            return redirect(url_for("secrets"))
        return render_template("secrets.html", user=new_user)


    return render_template("register.html")


@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        enter_password = request.form["password"]

        check_data = User.query.get("email")
        check_data


        return render_template("login.html")

    book_id = request.form["id"]
    book_to_update = Book.query.get(book_id)
    book_to_update.rating = request.form["rating"]
    db.session.commit()



@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static', "files/cheat_sheet.pdf", as_attachment=True)


@app.route('/base')
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
