# Import modules
from flask.globals import request
from flask_restplus import Resource, Namespace, api
from flask import Flask
from flask_marshmallow import Marshmallow
from marshmallow import *

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

review = api.model("Review",{
    "Comment": fields.String,
    "Rate":fields.String,
    "Date":fields.String,
    "UserId":fields.Integer,
    "BookId":fields.Integer,
})

tour = api.model("Review",{
    "Comment": fields.String,
    "Rate":fields.String,
    "Date":fields.String,
    "UserId":fields.Integer,
    "BookId":fields.Integer,
})



# Features Api
@namespace4.route("/review")
class ReviewResource(Resource):
    @namespace4.expect(review)
    def post(self):
        """
        Give Review to Tours
        """
        new_review = Review()
        new_review.Comment = request.json['Comment']
        new_review.Rate = request.json['Rate']
        new_review.UserId = request.json['UserId']
        new_review.Date = request.json['Date']
        new_review.BookId = request.json['BookId']

        bookId = Book.query.filter_by(book_id=new_review.BookId).first()
        userId = Book.query.filter_by(user_id=new_review.UserId).first()

        if (bookId & userId):
            db.session.add(new_review)
            db.session.commit()
            print(new_review)
            return review_schema.dump(new_review),201

        return 404

        



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



@namespace4.route("/tours/tourId:int")
class ToursResource(Resource):
    def get(self, tid):
        """
        Get Tour Details
        """
        
        tour = Tours.query.filter_by(book_id=tid).first()
        if tour:
            return tour_schema.dump(tour),200
        return 404   
