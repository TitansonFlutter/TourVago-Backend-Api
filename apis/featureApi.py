from datetime import datetime


from flask_restplus import Resource, fields, Namespace
from flask import request, Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace4 = Namespace("features", description="Features related operations")

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

tour_schema = TourSchema()
tours_schema = TourSchema(many=True)

review = namespace4.model(
    "Review",
    {
        "Comment": fields.String,
        "Rate": fields.Float,
        "Date": fields.String,
        "UserId": fields.Integer,
        "TourId": fields.Integer,
    },
)

tour = namespace4.model(
    "Tours",
    {
        "Comment": fields.String,
        "Rate": fields.String,
        "Date": fields.String,
        "UserId": fields.Integer,
        "BookId": fields.Integer,
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
        "Updated": fields.Boolean,
    },
)


# Features Api
@namespace4.route("/reviews")
class ReviewsResource(Resource):
    @namespace4.expect(review)
    def post(self):
        """
        Give Review to Tours
        """
        new_review = Review()
        new_review.Comment = request.json["Comment"]
        new_review.Rate = request.json["Rate"]
        new_review.UserId = request.json["UserId"]
        new_review.Date = request.json["Date"]
        new_review.TourId = request.json["TourId"]

        # bookId = Book.query.filter_by(book_id=new_review.TourId).first()
        userId = Book.query.filter_by(
            UserId=new_review.UserId, TourId=new_review.TourId
        ).first()

        if userId:
            db.session.add(new_review)
            db.session.commit()
            print(new_review)
            return review_schema.dump(new_review), 201

        return {"Message": "You are Not Booked Yet!!!"}, 404


@namespace4.route("/reviews/<int:tId>")
class ReviewResource(Resource):
    def get(self, tId):
        """
        Get A Tours Review
        """
        reviews = Review.query.filter_by(TourId=tId).all()
        if not reviews:
            return {"message": "There are no Reviews"}, 404
        lst = []
        for review in reviews:
            name = Users.query.filter_by(UserId=review.UserId).first()
            result = {
                "ReviewId": review.ReviewId,
                "UserId": review.UserId,
                "Comment": review.Comment,
                "Rate": review.Rate,
                "Date": review.Date,
                "Name": name.UserName,
                "TourId": review.TourId,
                "Date": review.Date,
            }

            lst.append(result)
        return lst, 200


@namespace4.route("/topDestinations")
class TopDestinationResource(Resource):
    def get(self):
        """
        Get Top Destinations
        """


@namespace4.route("/recommended")
class RecommendedResource(Resource):
    def get(self):
        """
        Get Recomenede Tours
        """
        tours = Tours.query.all()
        if not tours:
            return {"message": "No Tours"}, 404

        #  list
        lst = []
        # Check DateTime and if greater add to upcoming list
        for tour in tours:
            date = datetime.strptime(tour.StartingDate, "%Y-%m-%d %H:%M:%S.%f")

            if date >= datetime.now():
                # Get Tour Details from Database
                lst.append(tour)
        return tours_schema.dump(lst)


@namespace4.route("/tours/tourId:int")
class ToursResource(Resource):
    def get(self, tid):
        """
        Get Tour Details
        """
        # get tour detail
