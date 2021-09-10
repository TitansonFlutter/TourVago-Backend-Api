# Import modules
from flask_restplus import Resource, fields, Namespace
from flask import request, Flask
from flask_bcrypt import Bcrypt

# import jwt

# from flask_jwt_extended import (
#     create_access_token,
#     get_jwt,
#     jwt_required,
#     get_jwt_identity,
# )
from datetime import datetime
from Model.models import *
from marsh import *
import datetime

# Instance app
app = Flask(__name__)
bcrypt = Bcrypt(app)


app.config["SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
# app.config["JWT_SECRET_KEY"] = b'_5#y2L"F4Q8z\n\xec]/'
# app.config["JWT_BLACKLIST_ENABLED"] = ["access"]
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
        "Email": fields.String("Email"),
        "Role": fields.Integer(0),
        "Password": fields.String("Secured Password"),
    },
)

# Login User Data Model
login = namespace1.model(
    "Login", {"Email": fields.String("User Email"), "Password": fields.String}
)

# Auth Api
@namespace1.route("/login")
class UserResource(Resource):
    @namespace1.expect(login)
    def post(self):
        """
        Login user
        """
        expires = datetime.timedelta(days=30)

        # Get data from api
        email = request.json["Email"]
        password = request.json["Password"]
        print(email, password)
        # Get user data from database
        user = Users.query.filter_by(Email=email).first()
        # Check if the user exists
        if not user:
            return {"message": "The User is not Found"}, 404
        else:
            role = user.Role
            # Decrypt password from  database and compare
            check = bcrypt.check_password_hash(user.Password, password)
            # If the password is correct return user
            if check:
                additional_claims = {"role": role}
                # token = jwt.encode(
                #     {
                #         "user": user.UserId,
                #         "expiration": str(datetime.utcnow() + timedelta(seconds=60)),
                #     },
                #     app.config["SECRET_KEY"],
                # )
                # token = create_access_token(
                #     identity=user.UserId,
                #     expires_delta=expires,
                #     additional_claims=additional_claims,
                # )
                # return {"token": token.decode("utf-8")}
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
        new_user = Users()
        new_user.UserName = (request.json["UserName"],)
        new_user.Role = (request.json["Role"],)
        new_user.Email = (request.json["Email"],)
        new_user.Password = (hashed,)

        # Add to database
        db.session.add(new_user)
        db.session.commit()
        # Send user data
        return user_schema.dump(new_user), 201


@namespace1.route("/<int:id>")
class usersResource(Resource):
    def put(self, id):
        """
        Update User
        """
        email = request.json["Email"]
        user = Users.query.filter_by(Email=email).first()
        if user:
            return {"message": "User already exists"}, 400

        user = Users.query.filter_by(UserId=id).first()
        if not user:
            return {"message": "User not found"}, 404

        password = request.json["Password"]
        hashed = bcrypt.generate_password_hash(password).decode("utf-8")

        # new_user = Users()
        user.UserName = request.json["UserName"]
        user.Role = request.json["Role"]
        user.Email = request.json["Email"]
        user.Password = hashed

        db.session.commit()
        return user_schema.dump(user)
