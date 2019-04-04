# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session
from flask import Flask
from config import config


# 初始化mysql对象,可在之后用init_app导入app对象
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)

    # 初始化redis对象
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 开启CSRF防护
    CSRFProtect(app)

    # 初始化session对象
    Session(app)

    return app
