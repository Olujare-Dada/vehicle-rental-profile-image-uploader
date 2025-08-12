from flask import Flask
from controllers.image_controller import image_controller
from config.app_config import AppConfig



def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_controller, url_prefix='/image')
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=AppConfig().flask_host, port=AppConfig().flask_port)