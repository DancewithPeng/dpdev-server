from .db import db
from datetime import datetime
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import event, DDL

class UserInfo(db.Model) :        
    id          = db.Column(db.Integer, primary_key=True, comment='唯一标识')
    userid      = db.Column(db.Integer, nullable=False, comment='对应的用户ID')
    avatar      = db.Column(db.String(256), comment='头像')
    nickname    = db.Column(db.String(30), comment='昵称')
    valid       = db.Column(db.Boolean, default=True, nullable=False, comment='记录是否有效')
    updatetime  = db.Column(DATETIME(fsp=6), default=datetime.now, onupdate=datetime.now, nullable=False, comment='记录修改时间')