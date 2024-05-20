from flask import blueprints

oauth = blueprints.Blueprint("oauth", __name__)


@oauth.route("/login")
def login():
    return "login"
