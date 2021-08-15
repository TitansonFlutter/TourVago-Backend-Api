from flask_marshmallow import Marshmallow
from Model.models import *

# Instance
mar = Marshmallow()

# User Schema Model
class UsersSchema(mar.Schema):
    class Meta:
        fields = ("UserId", "UserName", "Role", "Email")

        model = Users


class Reviews:
    UserId = 0
    BookId = 0
    Comment = ""
    Rate = ""
    Date = ""


class ReviewSchema(mar.Schema):
    class Meta:
        fields = ("Comment", "Rate", "Date", "UserId", "BookId")
        model = Reviews


class Users:
    UserId = 0
    BookId = 0
    Comment = ""
    TourName = ""
    TourImage = ""
    Country = ""
    Region = ""
    City = ""
    WhatIsIncluded = ""
    WhatIsExcluded = ""
    TourDescription = ""
    WhatToBring = ""
    Itinerary = ""
    Duration = ""
    StartingDate = ""
    Special = ""
    Price = ""
    Updated = ""


class TourSchema (mar.Schema):
    class Meta:
        fields = (
            "UserId",
            "BookId",
            "Comment",
            "TourName",
            "TourImage",
            "Country",
            "Region",
            "City",
            "WhatIsIncluded",
            "WhatIsExcluded",
            "TourDescription",
            "WhatToBring",
            "Itinerary",
            "Duration",
            "StartingDate",
            "Special",
            "Price",
            "Updated"
        )
        model = Users
