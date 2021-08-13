# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace2 = Namespace("agents", description="Agents related operations")

# Agents Schema


# Agent Api
@namespace2.route("/agentId:int/agentInfo")
class AgentInfoResource(Resource):
    def post(self):
        """
        Add Agent Info
        """


@namespace2.route("")
class AgentsResource(Resource):
    def get(self):
        """
        Get all Agent
        """


@namespace2.route("/agentId:int/tour/tourId:int/")
class AgentTourResource(Resource):
    def get(self, agentId, tourId):
        """
        Get Tour
        """

    def put(self, agentId, tourId):
        """
        Update Tour
        """

    def delete(self, agentId, tourId):
        """
        Delete Tour
        """


# SignUP a User
@namespace2.route("/agentId:int/tours")
class AgentToursResource(Resource):
    def post(self, agentId):
        """
        Add  Tour
        """

    def get(self, agentId):
        """
        Get All Tours
        """


@namespace2.route("/agentId:int/history/historyId:int/")
class AgentHistoryResource(Resource):
    def get(self, agentId, historyId):
        """
        Get Tour
        """

    def delete(self, agentId, historyId):
        """
        Delete Tour
        """


@namespace2.route("/agentId:int/history")
class AgentsHistoryResource(Resource):
    def post(self, agentId):
        """
        Add  History
        """

    def get(self, agentId):
        """
        Get All Tours
        """


@namespace2.route("/agentId:int/reviews")
class AgentReviewsResource(Resource):
    def get(self, agentId):
        """
        Get All Tours
        """
