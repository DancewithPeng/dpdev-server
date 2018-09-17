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
    return context.get_current_parameters()['gentime']+timedelta(minutes=10)

# 访问令牌
class AccessToken(db.Model) :
    id          = db.Column(db.String(36), default=gen_uuid, primary_key=True, comment='唯一标识')
    client_id   = db.Column(db.String(36), nullable=False, comment='对应的客户端id')
    type        = db.Column(db.String(30), nullable=False, comment='AccessToken的类型，对应OAuth2.0的4种类型')
    userid      = db.Column(db.Integer, nullable=False, comment='对应的用户ID')
    terminal    = db.Column(db.String(36), nullable=False, comment='token适用的终端类型')
    gentime     = db.Column(DATETIME(fsp=6), default=datetime.now, nullable=False, comment='记录生成时间')
    expiretime  = db.Column(DATETIME(fsp=6), default=gen_expiretime, nullable=False, comment='记录过期时间')
    is_active   = db.Column(db.Boolean, default=True, nullable=False, comment='记录是否处于激活状态')

