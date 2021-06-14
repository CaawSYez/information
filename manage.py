# 此模块只作为入口函数,不进行其他操作,只放运行的命令
from flask import session
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from info import app,db


manager = Manager(app)  # 以命令行的形式,运行
Migrate(app, db)  # 将app与数据库关联,并迁移
manager.add_command("db", MigrateCommand)  # 给命令行添加迁移命令,db为迁移命令


@app.route("/")
def demo1():
    session["name"] = "liyang"
    return "hahha111"


if __name__ == '__main__':
    manager.run()
