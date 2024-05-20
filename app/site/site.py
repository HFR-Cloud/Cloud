from flask import blueprints, jsonify

site = blueprints.Blueprint("site", __name__)


@site.route("/ping")
def ping():
    data = {
        "code": 0,
        "data": "0.0.1",
        "msg": "HFR-Cloud Server is running!"
    }
    return jsonify(data)


@site.route("/config")
def config():
    data = {
        "code": 0,
        "data": {
            "title": "海枫云服务",
            "loginCaptcha": "false",
            "registerCaptcha": "false",
            "forgetCaptcha": "false",
            "captcha_type": "normal",
        },
        "msg": ""
    }
    return jsonify(data)