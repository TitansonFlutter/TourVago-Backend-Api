# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace3 = Namespace("users", description="Users related operations")


# User Api
@namespace3.route("/userId:int/book")
class ReviewsResource(Resource):
    def post(self, userId):
        """
        Add Agent Info
        """


@namespace3.route("/userId:int/history/upcoming")
class UserUpcomingHistoryResource(Resource):
    def get(self, userId):
        """
        Get Upcoming History
        """


@namespace3.route("/userId:int/history/past")
class UserPastHistoryResource(Resource):
    def get(self, userId):
        """
        Get Past History
        """
