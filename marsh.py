from flask_marshmallow import Marshmallow
from Model.models import *

# Instance
mar = Marshmallow()

# User Schema Model
class UsersSchema(mar.Schema):
    class Meta:
        fields = ("UserId", "UserName", "Role", "Email")

        model = Users
