from flask import Flask

from .access_token import AccessToken

def init_app(app: Flask) : 
    
    from .db import db
    db.init_app(app)
    
    with app.app_context():
        db.create_all()