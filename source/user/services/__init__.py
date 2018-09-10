# 服务层
from flask import Flask
from flask_restful import Api

def init_app(app: Flask) : 

    api = Api(app)

    from .root import Root
    from .signup import Signup

    api.add_resource(Root, '/')
    api.add_resource(Signup, '/signup/')