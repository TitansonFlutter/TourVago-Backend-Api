# Import modules
from flask_restplus import fields, Resource, Namespace
from flask import request, Flask
import datetime

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Users Namespace
namespace3 = Namespace("users", description="Users related operations")


# Book Data Model
book = namespace3.model(
    "Book",
    {"TourId": fields.Integer},
)


# Users Api
@namespace3.route("/userId:int/book")
class UserBookResource(Resource):
    @namespace3.expect(book)
    def post(self, userId):
        """
        Book A Tour
        """
        # Get Tour ID from Api
        tourId = request.json["TourId"]

        # Search if the Tour Exists
        tour = Tours.query.filter_by(TourId=tourId).first()

        # if no tour
        if not tour:
            return {"message": "The Tour Doesn't Exist"}, 400

        # create new Book
        new_book = Book(
            UserId=userId,
            TourId=tourId,
        )

        # Add to database
        db.session.add(new_book)
        db.session.commit()


@namespace3.route("/userId:int/history/upcoming")
class UserUpcomingHistoriesResource(Resource):
    def get(self, userId):
        """
        Get Upcoming History
        """

        # Get all user book histories
        histories = Book.query.filter_by(UserId=userId).all()

        # If not booked yet
        if not histories:
            return {"message": "You have not Booked Yet"}, 400

        # upcoming list
        upcoming = []
        # Check DateTime and if greater add to upcoming list
        for history in histories:
            date = history.StartingDate
            if date >= datetime.datetime.now():
                # Get Tour Details from Database
                tour = Tours.query.filter_by(TourId=history.TourId)
                upcoming.append(tour)

        return upcoming


@namespace3.route("/userId:int/history/past")
class UserPastHistoriesResource(Resource):
    def get(self, userId):
        """
        Get Past History
        """
        # Get all user book histories
        histories = Book.query.filter_by(UserId=userId).all()

        # If not booked yet
        if not histories:
            return {"message": "You have not Booked Yet"}, 400

        # past list
        past = []
        # Check DateTime and if less, add to past list
        for history in histories:
            date = history.StartingDate
            if date < datetime.datetime.now():
                # Get Tour Details from Database
                tour = Tours.query.filter_by(TourId=history.TourId)
                past.append(tour)

        return past
