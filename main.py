
from flask import Flask, render_template
from src.content import get_content
import sys

app = Flask(__name__)

names = []
status = {}


def generate(filename):
    global names
    global status
    names, status = get_content(filename)


@app.route("/")
def index():
    return render_template("index.html", data=names)


@app.route("/info/<name>")
def info(name):
    return render_template("info.html", data=status[name])


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "status.real"
    print(filename)
    generate(filename)
    app.run(host="0.0.0.0", port=5000)
