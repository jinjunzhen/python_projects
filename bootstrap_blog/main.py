from flask import Flask, render_template
import random
import datetime
import requests

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


#
# @app.route("/blog/<num>")
# def get_blog(num):
#     print(num)
#     blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
#     response = requests.get(blog_url)
#     all_posts = response.json()
#     return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
