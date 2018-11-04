from flask import Flask,render_template, request
from gettoken import reponse1
app = Flask(__name__)


@app.route('/')
def read():
    answer = request.args.get('response1')
    render_template("index.html")


if __name__ == '__main__':
    app.run()
