# Import modules
from flask_restplus import Resource, Namespace, fields
from flask import request, Flask


from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace2 = Namespace("agents", description="Agents related operations")


# AgentInfo Schema
agentInfo_schema = AgentInfosSchema()
agentInfos_schema = AgentInfosSchema(many=True)

# Tours Schema
tour_schema = ToursSchema()
tours_schema = ToursSchema(many=True)

# AgentInfo Data Model
agentInfo = namespace2.model(
    "AgentInfo",
    {
        "Approved": fields.String,
        "Acronym": fields.String,
        "Motto": fields.String,
        "Description": fields.String,
        "Website": fields.String,
        "Country": fields.String,
        "Region": fields.String,
        "City": fields.String,
        "Address": fields.String,
        "PhoneNumber": fields.String,
        "ZipCode": fields.String,
    },
)

# Tour Data Model
tour = namespace2.model(
    "Tour",
    {
        "TourName": fields.String,
        "TourImage": fields.String,
        "Country": fields.String,
        "Region": fields.String,
        "City": fields.String,
        "WhatIsIncluded": fields.String,
        "WhatIsExcluded": fields.String,
        "TourDescription": fields.String,
        "WhatToBring": fields.String,
        "Itinerary": fields.String,
        "Duration": fields.String,
        "StartingDate": fields.String,
        "Special": fields.String,
        "Price": fields.String,
        "Updated": fields.String,
    },
)


# Agent Api
@namespace2.route("/agentId:int/agentInfo")
class AgentInfoResource(Resource):
    @namespace2.expect(agentInfo)
    def post(self, agentId):
        """
        Add Agent Info
        """
        # Get data from api and create new instance of tour
        new_agentInfo = Tours(
            AgentId=agentId,
            Approved=request.json["Approved"],
            Acronym=request.json["Acronym"],
            Motto=request.json["Motto"],
            Description=request.json["Description"],
            Website=request.json["Website"],
            Country=request.json["Country"],
            Region=request.json["Region"],
            City=request.json["City"],
            Address=request.json["Address"],
            PhoneNumber=request.json["PhoneNumber"],
            ZipCode=request.json["ZipCode"],
        )
        # Add to database
        db.session.add(new_agentInfo)
        db.session.commit()
        # return tour data
        return tour_schema.dump(new_agentInfo), 200


# @namespace2.route("")
# class AgentsResource(Resource):
#     def get(self):
#         """
#         Get all Agent
#         """
#         agent = Users.query.filter_by(Role="Agent").all()
#         return users_schema.dump(agent), 200


@namespace2.route("/agentId:int/tour/tourId:int/")
class AgentTourResource(Resource):
    def get(self, agentId, tourId):
        """
        Get Tour
        """
        # Get tour data from database
        tour = Tours.query.filter_by(UserId=agentId, TourId=tourId).first()
        # Return tour data
        return tour_schema.dump(tour)

    @namespace2.expect(tour)
    def put(self, agentId, tourId):
        """
        Update Tour
        """
        # Get tour data from database
        tour = Tours.query.filter_by(UserId=agentId, TourId=tourId).first()

        tour.TourName = request.json["TourName"]
        tour.TourImage = request.json["TourImage"]
        tour.Country = request.json["Country"]
        tour.Region = request.json["Region"]
        tour.City = request.json["City"]
        tour.WhatIsIncluded = request.json["WhatIsIncluded"]
        tour.WhatIsExcluded = request.json["WhatIsExcluded"]
        tour.TourDescription = request.json["TourDescription"]
        tour.WhatToBring = request.json["WhatToBring"]
        tour.Itinerary = request.json["Itinerary"]
        tour.Duration = request.json["Duration"]
        tour.StartingDate = request.json["StartingDate"]
        tour.Special = request.json["Special"]
        tour.Price = request.json["Price"]
        tour.Updated = request.json["Updated"]
        tour.UserId = agentId

        # Add to database
        db.session.commit()
        # return tour data
        return tour_schema.dump(tour), 200

    def delete(self, agentId, tourId):
        """
        Delete Tour
        """
        # Get tour data from database
        tour = Tours.query.filter_by(UserId=agentId, TourId=tourId).first()
        # Delete from database
        db.session.delete(tour)
        db.session.commit()
        return tour_schema.dump(tour), 200


# SignUP a User
@namespace2.route("/agentId:int/tours")
class AgentToursResource(Resource):
    @namespace2.expect(tour)
    def post(self, agentId):
        """
        Add  Tour
        """
        # Get data from api and create new instance of tour
        new_tour = Tours(
            TourName=request.json["TourName"],
            TourImage=request.json["TourImage"],
            Country=request.json["Country"],
            Region=request.json["Region"],
            City=request.json["City"],
            WhatIsIncluded=request.json["WhatIsIncluded"],
            WhatIsExcluded=request.json["WhatIsExcluded"],
            TourDescription=request.json["TourDescription"],
            WhatToBring=request.json["WhatToBring"],
            Itinerary=request.json["Itinerary"],
            Duration=request.json["Duration"],
            StartingDate=request.json["StartingDate"],
            Special=request.json["Special"],
            Price=request.json["Price"],
            Updated=request.json["Updated"],
            UserId=agentId,
        )
        # Add to database
        db.session.add(new_tour)
        db.session.commit()
        # return tour data
        return tour_schema.dump(new_tour), 200

    def get(self, agentId):
        """
        Get All Tours
        """
        # Get every tours data from database
        tours = Tours.query.filter_by(UserId=agentId).all()
        # Return all tour data
        return tours_schema.dump(tours)


@namespace2.route("/agentId:int/history/historyId:int/")
class AgentHistoryResource(Resource):
    def get(self, agentId, historyId):
        """
        Get Tour
        """

    def delete(self, agentId, historyId):
        """
        Delete Tour
        """


@namespace2.route("/agentId:int/history")
class AgentsHistoryResource(Resource):
    def post(self, agentId):
        """
        Add  History
        """

    def get(self, agentId):
        """
        Get Tour History
        """


@namespace2.route("/agentId:int/reviews")
class AgentReviewsResource(Resource):
    def get(self, agentId):
        """
        Get Tour Reviews
        """
