# 用户模块
from flask import Flask

def init_app(app: Flask) :
    from . import models, services
    models.init_app(app)
    services.init_app(app)