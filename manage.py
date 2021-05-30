from flask import session
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.script import Manager
from flask_session import Session
from flask import Flask
from flask import request  # 从flask模块导入request后,就可以通过request.method查看请求方法
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect  # ext表示扩展的意思
from redis import StrictRedis

app = Flask(__name__)


class Config(object):  # 定义一个配置类,
    DEBUG = True  # 配置开发的模式
    # 使用session,一定要加密
    SECRET_KEY="qtnUZ1eG2zZv8JcD2tSTpiU7EsOZEHTCIY7CtZbiAZrU6wJcLJGahTt0j4kpdexP"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATION = False
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379  # 配置redis的端口和ip,一般都用大写
    SESSION_TYPE = "redis"  # 配置SESSION_TYPE,保存session的数据库类型
    SESSION_USE_SIGNER=True  # 使用Session签名,相当于加密操作.
    SESSION_REDIS=StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 指定Session保存的端口和ip
    SESSION_PERMANENT = False  # 默认是True,由于需要设置有效时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2  # 设置有效时间为2天,默认为31天



redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)  # 初始化redis对象
app.config.from_object(Config)  # 加载配置对象
db = SQLAlchemy(app)  # 初始化数据库对象
CSRFProtect(app)  # 对当前的项目开启保护机制,只有验证项目功能.针对patch post delete put请求
#设置Session保存位置
Session(app)
manager=Manager(app)  # 以命令行的形式,运行
Migrate(app,db)  # 将app与数据库关联,并迁移
manager.add_command("db",MigrateCommand)  # 给命令行添加迁移命令,db为迁移命令


@app.route("/")
def demo1():
    session["name"]="liyang"
    return "hahha"


if __name__ == '__main__':
    manager.run()