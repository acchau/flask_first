from exts import db


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # 设置外键 db.ForeignKey('author.id')，author 为表名
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    # 设置外键的关系，relationship 设置article关联用户author，backref 是反向关联
    author = db.relationship('Author', backref=db.backref('articles'))

    # 设置外键关系，多对多用secondary 来设置关联的中间表
    tags = db.relationship('Tag', secondary='article_tag', backref=db.backref('articles'))


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


# 多对多关系，设置中间表，用db.Table来实现
article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))
