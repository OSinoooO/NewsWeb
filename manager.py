# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    """项目配置"""
    DEBUG = True

    # mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:199577zhou@localhost:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = Flask

    # redis配置
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379


app = Flask(__name__)
app.config.from_object(Config)

# 初始化mysql对象
db = SQLAlchemy(app)

# 初始化redis对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF防护
CSRFProtect(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
