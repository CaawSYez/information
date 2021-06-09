# 此模块只作为入口函数,不进行其他操作
from flask import session
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.script import Manager
from flask_session import Session
from flask import Flask
from flask import request  # 从flask模块导入request后,就可以通过request.method查看请求方法
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect  # ext表示扩展的意思
from redis import StrictRedis
from config import Config
app = Flask(__name__)




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
    return "hahha111"


if __name__ == '__main__':
    manager.run()