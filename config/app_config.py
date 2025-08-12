from dotenv import load_dotenv
import os

load_dotenv()


class AppConfig:
    def __init__(self):
        self.FLASK_HOST = os.getenv('FLASK_HOST', '0.0.0.0')
        self.FLASK_PORT = os.getenv('FLASK_PORT', 5000)

    @property
    def flask_host(self) -> str:
        return self.FLASK_HOST
    
    @property
    def flask_port(self) -> int:
        return self.FLASK_PORT