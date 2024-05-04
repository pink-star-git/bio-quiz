from flask import Flask
from config import Config

app = Flask(__name__,
            static_url_path='',
            static_folder='')


app.config.from_object(Config)

from app.models import DB



from app import routes, models