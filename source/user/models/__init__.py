# 模型层
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

from .user import User
from .userinfo import UserInfo
from .token import Token
from .smscode import SMSCode

def init_app(app: Flask) :    
    from .db import db
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    