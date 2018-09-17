from flask import Flask, make_response, json
from flask_restful import Api

def init_app(app: Flask) : 
    
    api = Api(app)

    # 响应装饰器
    @api.representation('application/json')
    def output_json(data, code, headers=None):
        resp = make_response(json.dumps(data), code)        

        new_headers = {'Access-Control-Allow-Origin': '*',
                       'Access-Control-Allow-Headers': '*',
                       'Access-Control-Allow-Methods': '*'}
                       
        new_headers.update(headers or {})
        resp.headers.extend(new_headers)
        return resp

    from .access_token import APIAccessToken    
    api.add_resource(APIAccessToken, '/access-token/')