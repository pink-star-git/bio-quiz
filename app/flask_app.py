from flask import Flask
from config import Config

app = Flask(__name__,
            static_url_path='',
            static_folder='')


app.config.from_object(Config)

from . import routes