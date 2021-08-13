# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Admins Namespace
namespace6 = Namespace("admin", description="Admin related operations")


# Admin Api
@namespace6.route("/status/agents/agentId:int")
class AdminAgentResource(Resource):
    def put(self, agentId):
        """
        Update Agent Approval
        """

    def get(self, agentId):
        """
        Get Agent Approval
        """


@namespace6.route("/status/agents")
class AdminAgentsResource(Resource):
    def get(self):
        """
        Get All Agents Status
        """
