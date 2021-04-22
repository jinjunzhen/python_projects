# enter the following in terminal to run this project on http
# export FLASK_APP=app.py
# flask run -->(to run)
# control + C -->(to stop)



from flask import Flask, escape, request

app = Flask(__name__)





@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    app.run()