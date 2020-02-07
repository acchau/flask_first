# 相关拓展文件
from flask_sqlalchemy import SQLAlchemy
from flask import g

# 可以直接设置app db=SQLAlchemy
db = SQLAlchemy()


# 测试flask框架全部变量g的函数，无特别意义
def login_log():
    print('登陆的用户名是：', g.username)
    print('登陆用户的密码：', g.password)
