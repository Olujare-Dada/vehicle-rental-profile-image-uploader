from flask import Flask
from controllers.image_controller import image_controller
from config.app_config import AppConfig



def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_controller, url_prefix='/image')
    return app


# Create the app instance for gunicorn
app = create_app()

if __name__ == '__main__':
    app.run(host=AppConfig().flask_host, port=AppConfig().flask_port)