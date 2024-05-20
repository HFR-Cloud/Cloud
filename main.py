# coding:utf8

# 海枫云服务 服务端
# 作者: 于小丘

# 定义ASCII Logo
Logo = ("██╗  ██╗███████╗██████╗  ██████╗██╗      ██████╗ ██╗   ██╗██████╗\n"
        "██║  ██║██╔════╝██╔══██╗██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗\n"
        "███████║█████╗  ██████╔╝██║     ██║     ██║   ██║██║   ██║██║  ██║\n"
        "██╔══██║██╔══╝  ██╔══██╗██║     ██║     ██║   ██║██║   ██║██║  ██║\n"
        "██║  ██║██║     ██║  ██║╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝\n"
        "╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ")


# 导入Flask类
from flask import Flask
from app.OAuth import oauth
from app.site import site
from flask import send_from_directory
import os.path


# 创建Flask应用
app = Flask(__name__)


# 注册蓝图
app.register_blueprint(oauth, url_prefix="/api/oauth")
app.register_blueprint(site, url_prefix="/api/site")


# 客户端网页显示图标
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "assets"), "favicon.ico",
                               mimetype="image/vnd.microsoft.icon")


# 主程序
if __name__ == "__main__":
    print(Logo)
    app.run(port=7030, debug=True)
