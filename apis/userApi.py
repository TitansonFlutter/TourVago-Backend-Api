# Import modules
from flask_restplus import Resource, fields, Namespace
from flask import request, Flask
from flask_bcrypt import Bcrypt

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Users Namespace
namespace1 = Namespace("users", description="Users related operations")

# Users Schema
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


# User Data Model
user = namespace1.model(
    "User",
    {
        "UserName": fields.String("FirstName"),
        "Email": fields.String,
        "Password": fields.String("Secured Password"),
    },
)

# Login User Data Model
login = namespace1.model(
    "Login", {"Email": fields.String("User Email"), "Password": fields.String}
)

# User Api by Email
@namespace1.route("/<string:email>")
class userResource(Resource):
    def get(self, email):
        """
        Get user by email
        """
        user = Users.query.filter_by(Email=email).first()
        if not user:
            return {
                "message": "User not found for Email: {user_id}".format(user_id=email)
            }, 404

        return user_schema.dump(user)

    @namespace1.expect(user)
    @namespace1.response(204, "User successfully Updated.")
    def put(self, email):
        """
        Updates a user by email
        """
        user = Users.query.filter_by(Email=email).first()
        if not user:
            return {
                "message": "User not found for Email: {user_id}".format(user_id=email)
            }, 404

        user.FirstName = request.json["FirstName"]
        user.LastName = request.json["LastName"]
        user.Email = request.json["Email"]
        user.Password = request.json["Password"]

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user)


# Login User
@namespace1.route("/login")
class UserResource(Resource):
    @namespace1.expect(login)
    def post(self):
        """
        Login a user
        """
        email = request.json["Email"]
        password = request.json["Password"]

        user = Users.query.filter_by(Email=email).first()
        if not user:
            return {"message": "The Password or Email is Incorrect"}, 404
        else:
            check = bcrypt.check_password_hash(user.Password, password)
            if check:
                return user_schema.dump(user)
            else:
                return {"message": "The Password or Email is Incorrect"}, 400
