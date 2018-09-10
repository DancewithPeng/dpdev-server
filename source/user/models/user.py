from .db import db
from datetime import datetime
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy import event, DDL

# 用户
class User(db.Model) :
    id            = db.Column(db.Integer, primary_key=True, comment='唯一标识')
    username      = db.Column(db.String(30), nullable=False, index=True, comment='用户名')
    password      = db.Column(db.String(64), nullable=False, comment='密码')
    mobile_number = db.Column(db.String(20), comment='手机号')
    valid         = db.Column(db.Boolean, default=True, nullable=False, comment='记录是否有效')
    gentime       = db.Column(DATETIME(fsp=6), default=datetime.now, nullable=False, comment='记录创建时间') # fsp保留6位小数

# 在创建表完成后，设置自增长开始值
event.listen(User.__table__, 'after_create', DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 666666;"))
    