# -*- coding:utf-8 -*-
from . import index_blu
from info import redis_store


@index_blu.route('/')
def index():
    redis_store.set('hobby', 'game')
    return 'index'
