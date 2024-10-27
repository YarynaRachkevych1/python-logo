from flask import Blueprint, render_template, request, redirect

main = Blueprint('main', __name__)

@main.route('/', methods=["GET"])
def index_get() -> str:
    """GET endpoint for homepage.

    :return: Rendered template with homepage.
    """
    return render_template("index.html")

@main.route('/', methods=["POST"])
def index_post() -> str:
    """POST endpoint for homepage.

    :return: Redirect response to homepage.
    """
    code = request.form["code"]
    print(code)
    return redirect("/")
