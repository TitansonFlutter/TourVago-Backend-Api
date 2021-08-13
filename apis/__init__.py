from flask import Flask, Blueprint
from flask_restplus import Api
from flask_marshmallow import Marshmallow

from . import authApi, agentApi
from settings import *
from Model.models import *


# Flask Instance
app = Flask(__name__)

# configure database
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS


# Instantiate database
db.init_app(app)
ma = Marshmallow(app)


# Instantiate Blueprint
bp = Blueprint("api", __name__, url_prefix="/api")

# Instantiate Api
api = Api(
    bp,
    version="1.0",
    title="TourVago MobileApp API",
    description="API For A Tour Guide Mobile Application",
)


# Register the Blueprint
api.add_namespace(authApi.namespace1)

api.add_namespace(agentApi.namespace2)
app.register_blueprint(bp)
