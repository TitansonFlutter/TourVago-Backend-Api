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
namespace1 = Namespace("auth", description="Authentications related operations")

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

# Auth Api
# Login User
@namespace1.route("/login")
class UserResource(Resource):
    @namespace1.expect(login)
    def post(self):
        """
        Login user
        """
        # Get data from api
        email = request.json["Email"]
        password = request.json["Password"]

        # Get user data from database
        user = Users.query.filter_by(Email=email).first()
        # Check if the user exists
        if not user:
            return {"message": "The User is not Found"}, 404
        else:
            # Decrypt password from  database and compare
            check = bcrypt.check_password_hash(user.Password, password)
            # If the password is correct return user
            if check:
                return user_schema.dump(user)
            else:
                return {"message": "The Password or Email is Incorrect"}, 400


# SignUp User
@namespace1.route("")
class usersResource(Resource):
    # user user model
    @namespace1.expect(user)
    def post(self):
        """
        Create New User
        """
        # Get data from Api
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
        new_user = Users(
            UserName=request.json["UserName"],
            Role=request.json["Role"],
            Email=request.json["Email"],
            Password=hashed,
        )
        # Add to database
        db.session.add(new_user)
        db.session.commit()
        # Send user data
        return user_schema.dump(new_user), 200
