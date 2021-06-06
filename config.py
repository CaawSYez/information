# 专门用一个模块去设置配置
from  redis import StrictRedis
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

