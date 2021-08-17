# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Admins Namespace
namespace6 = Namespace("admin", description="Admin related operations")


class Agent(object):

    def __init__(self,name,username, password):
        self.name=name
        self.username=username
        self.password=password
    

    def __repr__(self):
        return 'This is agent {}'.format(self.name)

class AgentSchema(Schema):
    name =ma_fields.String()
    username=ma_fields.String()
    password=ma_fields.String()

    @post_load
    def create_Agent(self, data,**kwargs):
        return data



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
