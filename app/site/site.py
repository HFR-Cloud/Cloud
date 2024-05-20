from flask import blueprints

site = blueprints.Blueprint("site", __name__)


@site.route("/login")
def login():
    return "login"