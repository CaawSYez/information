# 业务逻辑的代码
from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from config import Config

app = Flask(__name__)

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)  # 初始化redis对象
app.config.from_object(Config)  # 加载配置对象
db = SQLAlchemy(app)  # 初始化数据库对象
CSRFProtect(app)  # 对当前的项目开启保护机制,只有验证项目功能.针对patch post delete put请求
# 设置Session保存位置
Session(app)