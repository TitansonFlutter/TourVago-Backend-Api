# Import modules
from flask_restplus import Resource, Namespace, fields,Api
from flask import Flask
from marshmallow import Schema,fields as ma_fields
from marshmallow.decorators import post_load
from Model.models import *
from marsh import *
import json


# Instance app
app = Flask(__name__)
api= Api(app)
# Admins Namespace
namespace6 = Namespace("admin", description="Admin related operations")



#class Agent

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





# Admin Agent Crud model
addAgent= namespace6.model(
    "Agent",
    {

    "name":fields.String(),
    "username":fields.String(),
    "password":fields.String()


    }
)


#sample  data
data =[]
agent =Agent(
    name="Lucy",
    username="L",
    password="67587t6"

    )
data.append(agent)
# Admin Api
@namespace6.route("/status/agents/agentId:int")


@namespace6.route("/status/agents")
class AdminAgentsResource(Resource):

    # @namespace6.marshal_with(addAgent,envelope='Data')
    
    def get(self):
        """
        Get All Agents Status
        """  
        schema = AgentSchema(many=True)
        return schema.dump(data)
        
