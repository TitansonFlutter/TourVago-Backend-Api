# Import modules
import datetime
import os, json
from flask_restplus import Resource, Namespace, fields
from flask import request, Flask, send_from_directory, make_response
from werkzeug.utils import secure_filename


from Model.models import *
from marsh import *
from .authApi import user_schema, users_schema

# Instance app
app = Flask(__name__)

UPLOAD_FOLDER = "./static/tours"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


ALLOWED_EXTENSIONS = set(["jpg", "jpeg", "gif", "png"])

# Check if allowed
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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
        "Price": fields.Integer,
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


@namespace2.route("")
class AgentsResource(Resource):
    def get(self):
        """
        Get all Agent
        """
        agent = Users.query.filter_by(Role=1).all()
        if not agent:
            return {"message": "There are no Agents!!!"}, 404

        return users_schema.dump(agent), 200


@namespace2.route("/<int:agentId>/tours/<int:tourId>")
class AgentTourResource(Resource):
    def get(self, agentId, tourId):
        """
        Get Tour
        """
        # Get tour data from database
        tour = Tours.query.filter_by(UserId=agentId, TourId=tourId).first()
        if not tour:
            return {"message": "There are no Tours"}, 404
        # Return tour data
        # filename = tour.TourImage
        # try:
        # with open(
        #     os.path.join(app.config["UPLOAD_FOLDER"], "response.jpeg"), "rb"
        # ) as fb:
        #     file = fb.read()
        #     response = make_response(file)
        #     response.headers.set("Content-Type", "multipart/form-data")
        #     return response
        #     return send_from_directory("../static/tours", filename, as_attachment=False)

        # except FileNotFoundError:
        #     return {"message": "File not found"}, 404
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
        if not tour:
            return {"Message": "Tour dose not exist"}, 404
        # Delete from database
        db.session.delete(tour)
        db.session.commit()
        return {"message": "Deleted"}, 200


# SignUP a User
@namespace2.route("/<int:agentId>/tours")
class AgentToursResource(Resource):
    @namespace2.expect(tour)
    def post(self, agentId):
        """
        Add  Tour
        """
        data = json.loads(request.values["data"])
        # print(data["TourName"])

        agent = Users.query.filter_by(UserId=agentId).first()
        if agent.Role != 1:
            return {"message": "You are not an Agent!!!"}, 400
        # Get data from api and create new instance of tour

        if "pic" not in request.files:
            return {"message": "No Image File was Sent"}, 400

        image = request.files["pic"]
        if not image or not allowed_file(image.filename):
            return {"message": "File type not allowed"}, 400

        else:
            filename = secure_filename(image.filename)
            path = os.path.join(
                app.config["UPLOAD_FOLDER"] + "/" + agent.UserName, filename
            )
            image.save(path)
            print(filename)

            new_tour = Tours(
                TourName=data["TourName"],
                TourImage=filename,
                Country=data["Country"],
                Region=data["Region"],
                City=data["City"],
                WhatIsIncluded=data["WhatIsIncluded"],
                WhatIsExcluded=data["WhatIsExcluded"],
                TourDescription=data["TourDescription"],
                WhatToBring=data["WhatToBring"],
                Itinerary=data["Itinerary"],
                Duration=data["Duration"],
                StartingDate=data["StartingDate"],
                Price=data["Price"],
                Updated=data["Updated"],
                UserId=agentId,
            )
            # Add to database
            db.session.add(new_tour)
            db.session.commit()
        # return tour data
        return tour_schema.dump(new_tour), 200
        # return "Success", 200

    def get(self, agentId):
        """s
        Get All Tours
        """
        # Get every tours data from database
        tours = Tours.query.filter_by(UserId=agentId).all()
        if not tours:
            return {"message": "You Have no tours"}, 404

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


@namespace2.route("/images/<imageName>")
class AgentsHistoryResource(Resource):
    def post(self):
        """
        Add  History
        """

    def get(self, imageName):
        """
        Get Tour History
        """
        print(imageName)
        return send_from_directory(
            "../static/tours/Exodes", imageName, as_attachment=False
        )


@namespace2.route("/agentId:int/reviews")
class AgentReviewsResource(Resource):
    def get(self, agentId):
        """
        Get Tour Reviews
        """
