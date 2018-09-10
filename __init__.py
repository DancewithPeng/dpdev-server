from flask import Flask
import os

# App工厂
def create_app(config=None) : 

    app = Flask(__name__)

    # 配置

    # 默认配置
    app.config.from_pyfile('config/default_config.py')

    # instance中的配置
    app.config.from_pyfile('instance/default_config.py')

    # 环境配置
    if 'FLASK_ENV' in os.environ:
        app.config.from_envvar('FLASK_ENV')

    # 指定配置
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    # 业务模块

    print('ahahha')

    from .source import user    
    user.init_app(app)
    #access.init_app(app)
    #interactive.init_app(app)    
    return app

# gunicorn 启动需要创建对应的实例
app = create_app()

# 启动
if __name__ == '__main__':
    app.run()        