from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from flask_cors import CORS




app = Flask(__name__)
app.config.from_object(config)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server import routes, models

if not app.debug: 
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    app.logger.addHandler(stream_handler)


app.logger.setLevel(logging.INFO)
app.logger.infor('Flask App startup')