from .db import db
from datetime import datetime
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import event, DDL

def gen_expiretime(context) :
    return context.get_current_parameters()['gentime']+timedelta(minutes=10)

class SMSCode(db.Model) :
    id            = db.Column(db.Integer, primary_key=True, comment='唯一标识')
    userid        = db.Column(db.Integer, nullable=False, comment='对应的用户ID')
    mobile_number = db.Column(db.String(20), nullable=False, comment='手机号码')
    code          = db.Column(db.Integer, nullable=False, comment='验证码')
    gentime       = db.Column(DATETIME(6), default=datetime.now, nullable=False, comment='记录生成时间')
    expiretime    = db.Column(DATETIME(6), default=gen_expiretime, nullable=False, comment='记录过期时间')
    isactive      = db.Column(db.Boolean, default=True, nullable=False, comment='记录是否处于激活状态')