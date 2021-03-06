from flask_restful import Resource, request, reqparse
from ..models.user import User
from ..models.db import db
import re

# 注册
class Signup(Resource) :

    def __init__(self): 
        self.param_parser = reqparse.RequestParser() # 创建参数解析器
        self.param_parser.add_argument('username', type=str, required=True)
        self.param_parser.add_argument('password', type=str, required=True)
        self.param_parser.add_argument('Platform', type=str, location='headers', required=True)
        self.param_parser.add_argument('App', type=str, location='headers', required=True)

    def post(self) :

        params = self.param_parser.parse_args(strict=True)
        username = params['username']
        password = params['password']
        platform_header = params['Platform']
        app_header = params['App']
        
        # 参数错误
        if len(username) <= 0 or len(password) <= 0 or len(platform_header) <= 0 or len(app_header) <= 0 :            
            return {'message': '参数错误'}, 400

        # 用户名校验正则表达式
        username_regex = '^[a-zA-Z]{1}([a-zA-Z0-9]|[_]){5,30}$' # 字母数字下划线，字母开头
        password_regex = '^[a-zA-Z0-9]{64}$'                    # sha256

        u_match = re.match(username_regex, username)
        p_match = re.match(password_regex, password)                                           
                
        # 参数格式不正确
        if u_match is None or p_match is None :
            return {'message': '用户名或密码格式错误'}, 10101       
        
        # 查询
        if User.query.filter_by(username=username).first() is not None : # 用户名已经存在
            return {'message': '用户名已存在'}, 10102
            
        try:              
            # 插入
            user = User()
            user.username = username
            user.password = password            
            
            db.session.add(user)
            db.session.commit()

        except Exception as error:
            db.session.rollback()        

            return {'message': '服务器异常，请联系管理员'}, 500
            
        # 返回值是一个元组：(内容，响应码，响应头)
        return {'message': 'OK'}, 201