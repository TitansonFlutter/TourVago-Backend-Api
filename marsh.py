from flask_marshmallow import Marshmallow
from Model.models import *

mar = Marshmallow()


class UsersSchema(mar.Schema):
    class Meta:
        fields = ("FirstName", "LastName", "Email")

        model = Users
