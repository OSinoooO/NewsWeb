# -*- coding:utf-8 -*-
from flask import Blueprint

# 创建蓝图对象
index_blu = Blueprint('index', __name__)

# 与views关联
from . import views
