# flask_script 用来设置开发服务器 数据库设置 定时任务
# 问题点，在虚拟环境中安装的mysql-connector-python 用终端命令执行会引用不到，需要安装全局的mysql-connector-python
# 因为mysql8 默认的密码加密方式是用caching_sha2_password

from flask_script import Manager
from app import app
# from db_script import DBManage
from flask_migrate import Migrate, MigrateCommand
from exts import db
from models import *

manage = Manager(app)


# 直接执行命令  python manage.py runserver
@manage.command
def runserver():
    print('服务跑起来了')


# 设置子命令 python manage.py db init/migrate
# manage.add_command('db', DBManage)

# flask_migrate需要配合flask_script来使用
# 使用flask_migrate实现数据库迁移，当model新增属性时，执行相关命令来实现表字段的新增
# 要使用flask_migrate 必须要绑定app 和db
migrate = Migrate(app, db)

# 把MigrateCommand相关命令添加到manage中
# 先执行 init命令初始化迁移（只需要执行一次即可）python manage.py db init
# 再执行 migrate命令生产迁移文件（model新增新的属性时执行）python manage.py db migrate
# 再执行 upgrade命令完成迁移操作（migrate命令执行后再执行）python manage.py db upgrade

manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
