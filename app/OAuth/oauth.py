from flask import request, jsonify, blueprints


oauth = blueprints.Blueprint("oauth", __name__)


@oauth.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    data = {
        "code": 0,
        "data": {
            "username": username,
            "password": password
        },
        "msg": ""
    }
    return jsonify(data)


@oauth.route("/register")
def register():
    return "register"
