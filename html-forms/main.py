from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/log_in', methods=["POST"])
def receive_data():
    name1 = request.form['name1']
    password1 = request.form['password1']
    return render_template('log_in.html', name1=name1, password1=password1)


@app.route('/<num>')
def get_blog(num):
    return render_template('post.html', num=num,
                           bolg1_title="this is the blog title",
                           bolg1_body="this is the blog body")


if __name__ == "__main__":
    app.run(debug=True)
