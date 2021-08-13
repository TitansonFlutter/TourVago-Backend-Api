# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace6 = Namespace("admin", description="Admin related operations")


# Admin Api
@namespace6.route("/status/agents/agentId:int")
class ReviewsResource(Resource):
    def put(self):
        """
        Update Agent Info
        """

    def get(self):
        """
        Add Agent Info
        """


@namespace6.route("/status")
class ReviewsResource(Resource):
    def get(self):
        """
        Add Agent Info
        """
