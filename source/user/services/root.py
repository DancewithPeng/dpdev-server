from flask import jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
import hashlib

from ..models.user import User
from ..models.db import db

class Root(Resource) :
    def get(self):

        u1 = User()
        u1.username = 'zhangpeng'
        u1.password = hashlib.sha256('dpdev666'.encode('utf-8')).hexdigest()

        db.session.add(u1)
        db.session.commit()
                                
        return jsonify({'msg': 'OK'})