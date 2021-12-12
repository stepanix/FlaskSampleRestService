from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# create the application database instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.domain.models import product_models, cart_model
from app.routes import product_route


