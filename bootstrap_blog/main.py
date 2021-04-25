from flask import Flask, render_template, request
import requests
import smtplib

my_email = 'jinjunzhen.testing'
password = 'abcd1234()()'

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/send_email", methods=["POST"])
def send_email():
    name1 = request.form['name1']
    email1 = request.form['email1']
    phone1 = request.form['phone1']
    message1 = request.form['message1']

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email1,
            msg=f'Subject: dear {name1} \n\n phone number: {phone1} {message1}'
        )

    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
