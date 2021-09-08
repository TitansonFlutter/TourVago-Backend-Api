# Import modules
from flask_restplus import Resource, Namespace, fields, Api
from flask import Flask, request

# from marshmallow import Schema,fields as ma_fields
# from marshmallow.decorators import post_load
from Model.models import *
from marsh import *
from .authApi import user_schema, users_schema, bcrypt


# Instance app
app = Flask(name)
api = Api(app)
# Admins Namespace
namespace6 = Namespace("admin", description="Admin related operations")


# class Agent
# class Agent(object):

#     def init(self,name,username, password):
#         self.name=name
#         self.username=username
#         self.password=password


#     def repr(self):
# return 'This is agent {}'.format(self.name)

# class AgentSchema(Schema):
#     name =ma_fields.String()
#     username=ma_fields.String()
#     password=ma_fields.String()

#     @post_load
#     def create_Agent(self, data,**kwargs):
#         return data


# Admin Agent Crud model
addAgent = namespace6.model(
    "Agent",
    {
        "UserName": fields.String("FirstName"),
        "Email": fields.String("Email"),
        "Role": fields.Integer(1),
        "Password": fields.String("Secured Password"),
    },
)


# sample  data
# data =[]
# agent =Agent(
#     name="Lucy",
#     username="L",
#     password="67587t6"

#     )
# data.append(agent)

# Admin Api
@namespace6.route("/status/agents/agentId:int")
class AdminAgentStatusResource(Resource):
    @namespace6.expect(addAgent)
    def put(self):

        """
        Update Agent Approval
        """
        # schema= AgentSchema()
        # newAgent =schema.load(api.payload)
        # data.append(newAgent)
        # print(newAgent)

        # return {"Result":"New Agent added successfully ..."},201

    def get(self, agentId):
        """
        Get Agent Approval
        """
        result = {"Name": "Abebe"}
        print(result)

        return {"Result": result}


@namespace6.route("/status/agents")
class AdminAgentsStatusResource(Resource):

    # @namespace6.marshal_with(addAgent,envelope='Data')

    def get(self):
        """
        Get All Agents Status
        """
        # schema = AgentSchema(many=True)
        # return schema.dump(data)


@namespace6.route("/agents")
class AdminAgentsResource(Resource):
    @namespace6.expect(addAgent)
    def post(self):
        """
        Add Agents
        """
        email = request.json["Email"]
        password = request.json["Password"]

        #  get user from database
        user = Users.query.filter_by(Email=email).first()
        # Check if the user already exists
        if user:
            return {"message": "The Email Address already exists"}, 400

        # Hash the password
        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        # Create Instance
        new_user = Users()
        new_user.UserName = request.json["UserName"]
        new_user.Role = request.json["Role"]
        new_user.Email = request.json["Email"]
        new_user.Password = hashed

        # Add to database
        db.session.add(new_user)
        db.session.commit()
        # Send user data
        return user_schema.dump(new_user), 201

    def get(self):
        """
        Get All Agents
        """
        # get all agents
        agents = Users.query.filter_by(Role=1).all()
        if not agents:
            return {"message": "No Agents are Added"}, 404
        return users_schema.dump(agents)


@namespace6.route("/agents/<int:agentId>")
class AdminAgentResource(Resource):
    def get(self, agentId):
        """
        Get agent by ID
        """
        agent = Users.query.filter_by(Role=1, UserId=agentId).first()
        if not agent:
            return {"message": "Agent does not exist!!"}, 404
        return users_schema.dump(agent)

    def delete(self, agentId):
        """
        Delete Agents by ID
        """
        agent = Users.query.filter_by(Role=1, UserId=agentId).first()
        if not agent:
            return {"message": "Agent does not exist!!"}, 404

        db.session.delete(agent)
        db.session.commit()
        return {"message": "Successfully Deleted"}, 200