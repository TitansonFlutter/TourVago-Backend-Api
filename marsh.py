from flask_marshmallow import Marshmallow
from Model.models import *

mar = Marshmallow()


class UsersSchema(mar.Schema):
    class Meta:
        fields = ("UserId", "UserName", "Role", "Email")

        model = Users
