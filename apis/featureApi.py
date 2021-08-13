# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace4 = Namespace("feature", description="Features related operations")


# User Api
@namespace4.route("/review")
class ReviewResource(Resource):
    def post(self):
        """
        Give a Review to Tours
        """


@namespace4.route("/topDestinations")
class TopDestinationResource(Resource):
    def get(self):
        """
        Add Agent Info
        """


@namespace4.route("/recommended")
class RecommendedResource(Resource):
    def get(self):
        """
        Add Agent Info
        """


@namespace4.route("/tours/tourId:int")
class ToursResource(Resource):
    def get(self):
        """
        Add Agent Info
        """
