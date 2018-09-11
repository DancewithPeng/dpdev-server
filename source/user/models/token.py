from .db import db
from datetime import datetime, timedelta
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import event, DDL

import uuid

# 生成uuid
def gen_uuid() :
    return str(uuid.uuid4())

# 生成过期时间
def gen_expiretime(context) :
    return context.get_current_parameters()['gentime']+timedelta(days=7)

class Token(db.Model) :
    id          = db.Column(db.String(36), default=gen_uuid, primary_key=True, comment='唯一标识')
    userid      = db.Column(db.Integer, nullable=False, comment='对应的用户ID')
    terminal    = db.Column(db.String(36), nullable=False, comment='token适用的终端类型')
    gentime     = db.Column(DATETIME(fsp=6), default=datetime.now, nullable=False, comment='记录生成时间')
    expiretime  = db.Column(DATETIME(fsp=6), default=gen_expiretime, nullable=False, comment='记录过期时间')
    isactive    = db.Column(db.Boolean, default=True, nullable=False, comment='记录是否处于激活状态')

