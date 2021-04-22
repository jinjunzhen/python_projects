# enter the following in terminal to run this project on http
# export FLASK_APP=app.py
# flask run -->(to run)
# control + C -->(to stop)



from flask import Flask, escape, request

app = Flask(__name__)


def make_bold(function):
    def the_bold():
        return f"<b>{function()}</b>"
    return the_bold



@app.route('/bye')
@make_bold
def say_bye():
    return "Bye!"


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/<name>')
def greeting(name):
    return f"What's up {name}"

if __name__ == "__main__":
    app.run(debug=True)