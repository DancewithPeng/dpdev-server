from flask_restful import Resource, request, reqparse
from flask import jsonify
from ..models.user import User
from ..models.db import db

# 注册
class Signup(Resource) :

    def __init__(self): 
        self.param_parser = reqparse.RequestParser() # 创建参数解析器
        self.param_parser.add_argument('username', type=str)
        self.param_parser.add_argument('password', type=str)

    def post(self) :
        params = self.param_parser.parse_args()
        username = params['username']
        password = params['password']

        if username is not None and len(username) > 0 and password is not None and len(password) > 0 :
            
            try:
                user = User()
                user.username = username
                user.password = password
            
                db.session.add(user)
                db.session.commit()
            except expression as identifier:
                return {'message': '服务器挂啦'}, 500, {'Custom-Header': 'hahahah'}
        
        else :
            return {'message': '请传合适的参数'}, 500, {'Custom-Header': 'hahahah'}
            
        # 返回值是一个元组：(内容，响应码，响应头)
        return {'message': 'OK'}, 201, {'Custom-Header': 'hahahah'}