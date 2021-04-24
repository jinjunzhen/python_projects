from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<num>')
def get_blog(num):
    return render_template('post.html', num=num,
                           bolg1_title="this is the blog title",
                           bolg1_body="this is the blog body")

if __name__ == "__main__":
    app.run(debug=True)
