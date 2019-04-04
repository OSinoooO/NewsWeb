# -*- coding:utf-8 -*-
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = '2UKGQoGlL3qo16EHBoHmgVoWEULUMp+4lUp7vUjQ2mqJIPWI6u+yiT4pYlFlQAHi'

    # mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:199577zhou@localhost:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask

    # redis配置
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379

    # session配置
    # session保存位置
    SESSION_TYPE = 'redis'
    # 指定保存session的redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 设置可过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)
app.config.from_object(Config)

# 初始化mysql对象
db = SQLAlchemy(app)

# 初始化redis对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF防护
CSRFProtect(app)

# 初始化session对象
Session(app)

manager = Manager(app)

# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = 'osin'
    return 'index'


if __name__ == '__main__':
    manager.run()
