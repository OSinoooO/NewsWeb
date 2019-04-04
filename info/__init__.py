# -*- coding:utf-8 -*-
from logging.handlers import RotatingFileHandler
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session
from flask import Flask
from config import config
import logging


# 初始化mysql对象,可在之后用init_app导入app对象
db = SQLAlchemy()


def setup_log(config_name):
    """创建日志"""
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 输出日志等级
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024 * 1024 * 1024, backupCount=10)  # 日志记录器
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')  # 日志格式
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)  # 为全局日志工具对象添加日志记录器


def create_app(config_name):
    """创建app"""
    setup_log(config_name)
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
