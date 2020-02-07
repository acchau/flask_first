from  datetime import timedelta

DEBUG = True

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = 'qq1031431322'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_env'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# session 密钥
SECRET_KEY = 'eC6vffOoKVwSlh+W/GxQCeEeeJOGoXgyyzWgiuvSWCLVq91YrABsgfxZS2ww19cSU3uMXno5QJ0PZPDdnnljJ4yA'

# session 过期时间 permanent值设置为True 时有效，否则 默认关闭浏览器就失效，PERMANENT_SESSION_LIFETIME默认值时31天
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
