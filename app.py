from flask import Flask, redirect, url_for, render_template, session, request, g
from models import *
from exts import db, login_log

import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# db.create_all() 直接用db = SQLAlchemy(app)可以这样使用；db.create_all()目的是通过model来创建表
# model分离写到其他的地方，就需要手动添加上下文，否则会报错
# No application found. Either work inside a view function or push an application context.
# with app.app_context():
#     db.create_all()
# db.create_all() 只会执行一次，当你修改来model属性时，它不会自动增加相关属性，需要用数据库迁移来实现更新model对应表的字段


@app.route('/')
def hello_world():
    # print(url_for("my_list"))
    # print(url_for('article', id="1234"))
    # flask_sqlalchemy相关使用
    # 增
    # article1 = Article(title='测试数据', content='测试数据的内容')
    # db.session.add(article1)
    # db.session.commit()

    # 查
    # result = Article.query.filter(Article.title == '测试数据').first()
    # print(result.title)
    # print(result.content)

    # 改
    # article_result = Article.query.filter(Article.title == '测试数据').first()
    # article_result.title = '修改后的测试数据'
    # db.session.commit()

    # 删
    # article_result = Article.query.filter(Article.title == '修改后的测试数据').first()
    # db.session.delete(article_result)
    # db.session.commit()

    # 外键设置和使用
    # author = Author(username='周勇利')
    # db.session.add(author)
    # db.session.commit()
    #
    # article_res = Article(title='活着', content='活着才有机会做更多的事情', author_id=1)
    # article_result = Article(title='好好努力', content='世间不会亏待每个有心人', author_id=1)
    # db.session.add(article_res)
    # db.session.add(article_result)
    # db.session.commit()

    # 通过article来获取作者
    # article_res = Article.query.filter(Article.title == '活着').first()
    # print(article_res.author.username)

    # 通过author 来查找用户所有的文章
    # author_result = Author.query.filter(Author.username == '周勇利').first()
    # articles = author_result.articles

    # for art in articles:
    #     print('-'*10)
    #     print(art.title)

    # 多对多关系对象新增
    # tag1 = Tag(name='生活')
    # tag2 = Tag(name='情感')
    #
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # article_res = Article.query.filter(Article.title == '活着').first()
    # article_res.tags.append(tag1)
    # article_res.tags.append(tag2)
    #
    # db.session.commit()

    # 多对多关系查找
    if hasattr(g, 'username'):
        article_result = Article.query.filter(Article.title == '活着').first()
        tags = article_result.tags
        for t in tags:
            print('*' * 10)
            print(t.name)
        # session 设置，flask框架的session是经过加密后返回给浏览器保存在cookie中
        # session['tag'] = '生活和情感'
        return 'hello world!'
    else:
        return redirect(url_for('login'))


@app.route('/get/')
def get():
    # session 获取
    tag = session.get('tag')
    print(tag)
    # session 删除
    if tag:
        print('key->tag存在')
        session.pop('tag')
    else:
        print('key->tag不存在')

    print(session.get('tag'))
    return 'success'


@app.route('/article/<id>')
def article(id):
    return u'你传入的参数是：%s' % id


@app.route('/list/')
def my_list():
    return


@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return u'这是发布问答页面'
    else:
        return redirect(url_for('login'))


# methods 参数设置post和get访问类型 ，默认只支持get访问
# get 可以使用request.args.get('')获取参数
# post 可以使用request.form.get('')获取参数
@app.route('/login/', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        q = request.args.get('q')
        print('get的请求参数：', q)
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')

        if username == '123456' and password == '123456':
            # # g 是flask框架的全局变量，在一次请求中全局有效，请求结束后g就会失效
            # g.username = username
            # g.password = password
            # # 使用来全局变量g的方法，必须在同一次调用中使用，调用完成就回被释放掉
            # login_log()

            # 用来验证钩子函数 before_request
            session['username'] = username
            return redirect(url_for('hello_world'))
        else:
            return u'用户名密码错误'


@app.route('/index/')
def index():
    class Person(object):
        name = u'周勇利'
        age = 29

    p = Person()

    context = {
        'username': u'周勇利',
        'sex': u'男',
        'age': 29,
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)


@app.route('/answer/<id>')
def answer(id):
    user = {
        'name': u'周勇利',
        'age': 29
    }
    if id == '1':
        return render_template('answer.html', user=user)
    else:
        return render_template('answer.html')


@app.route('/for/')
def my_for():
    user = {
        'username': u'周勇利',
        'age': 29
    }

    websites = ['www.baidu.com', 'www.google.com']

    books = [
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': 120
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': 123
        },
        {
            'name': '三国演义',
            'author': '罗贯中',
            'price': 124
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
            'price': 125
        }
    ]

    avatar = ''

    contents = [
        {
            'name': '周勇利',
            'text': '评论内容'
        },
        {
            'name': '周劭洋',
            'text': '评论内容2'
        }
    ]

    return render_template('for.html', user=user, websites=websites, books=books, contents=contents)


@app.route('/extend_block/')
def extend_block():
    return render_template('extendblock.html')


@app.before_request
def my_before_request():
    # 在所有的视图函数之前执行
    # 可以做一些登陆之前的验证，判断用户是否已经登陆，不能在钩子函数中直接使用redirect，会导致重复的重定向
    username = session.get('username')
    if username:
        g.username = username


@app.context_processor
def my_context_processor():
    # 上下文处理程序，可以设置字典，字典的key值会被模版当作变量来处理，
    # 作用是多个模版有共同的变量时可以在上下文处理程序中设置
    return {'username':  '周勇利'}


if __name__ == '__main__':
    app.run()
