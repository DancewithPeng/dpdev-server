# 服务层
from flask import Flask
from flask_restful import Api

def init_app(app: Flask) : 

    api = Api(app)

    from .signup import Signup    
    from .password_auth import PasswordAuth

    api.add_resource(Signup, '/signup/')
    api.add_resource(PasswordAuth, '/auth/password/')