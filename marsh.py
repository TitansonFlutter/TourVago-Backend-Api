from flask_marshmallow import Marshmallow
from Model.models import *

# Instance
mar = Marshmallow()

# User Schema Model
class UsersSchema(mar.Schema):
    class Meta:
        fields = ("UserId", "UserName", "Role", "Email")

        model = Users
# Tour Schema Model
class ToursSchema(mar.Schema):
    class Meta:
        fields = ("TourId", "TourName", "TourImage", "Country", "Region", "City", "WhatIsIncluded", "WhatIsExcluded", "TourDescription", "WhatToBring", "Itinerary", "Duration", "StartingDate", "Special", "Price", "Updated", "UserId")

        model = Tours

# AgentInfo Schema Model
class AgentInfosSchema(mar.Schema):
    class Meta:
        fields = ("AgentInfoId", "AgentId", "Approved", "Acronym", "Motto", "Description", "Website", "Country", "Region", "City", "Address", "PhoneNumber", "ZipCode")

        model = AgentInfo
