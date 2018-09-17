from flask_restful import Resource, request, reqparse
from ..models.access_token import AccessToken
from ..models.db import db
import re

class APIAccessToken(Resource) :
    def post(self) :
        return {"message": "Hello!"}, 200