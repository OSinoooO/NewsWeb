# -*- coding:utf-8 -*-
from redis import StrictRedis


class Config(object):
    """项目配置"""
    SECRET_KEY = '2UKGQoGlL3qo16EHBoHmgVoWEULUMp+4lUp7vUjQ2mqJIPWI6u+yiT4pYlFlQAHi'

    # mysql配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:199577zhou@localhost:3306/news'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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


class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = 'WARNING'


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True
    LOG_LEVEL = 'DEBUG'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}