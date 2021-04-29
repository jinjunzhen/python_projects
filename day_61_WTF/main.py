# from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from flask_ckeditor import CKEditor, CKEditorField


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"



class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = MyForm()
    login_form.validate_on_submit()
    print(login_form.email.data)
    print(login_form.password.data)
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)