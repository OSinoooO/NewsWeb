# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask_session import Session
from flask import Flask
from Config import Config


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
