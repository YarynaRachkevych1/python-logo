from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=["GET"])
def index_get():
    return render_template("index.html")

@main.route('/', methods=["POST"])
def index_post():
    code = request.form["code"]
    print(code)
    return render_template("index.html")