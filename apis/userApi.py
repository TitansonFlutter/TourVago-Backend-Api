
# Import modules
from flask_restplus import fields, Resource, Namespace
from flask import request, Flask
from datetime import datetime

from Model.models import *
from marsh import *
from .agentApi import tour_schema, tours_schema
from .authApi import user_schema

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
@namespace3.route("/<int:userId>/book")
class UsersBookResource(Resource):
    @namespace3.expect(book)
    def post(self, userId):
        """
        Book A Tour
        """
        # Get Tour ID from Api
        tourId = request.json["TourId"]

        # Search if the Tour Exists
        tour = Tours.query.filter_by(TourId=tourId).first()
        print(tour)

        # if no tour
        if not tour:
            return {"message": "The Tour Doesn't Exist"}, 400

        book = Book.query.filter_by(UserId=userId, TourId=tourId).first()
        if book:
            return {"message": "You have allready Booked"}, 400
        # create new Book
        new_book = Book(
            UserId=userId,
            TourId=tourId,
        )

        # Add to database
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Booked"}, 200


@namespace3.route("/<int:userId>/book/<int:tourId>")
class UserBookResource(Resource):
    def get(self, userId, tourId):
        """
        book status
        """
        book = Book.query.filter_by(UserId=userId, TourId=tourId).first()
        if book:
            user = Users.query.filter_by(UserId=userId).first()

            return user_schema.dump(user)
        return {"message": "Not Booked"}, 404


@namespace3.route("/<int:userId>/history/upcoming")
class UserUpcomingHistoriesResource(Resource):
    def get(self, userId):
        """
        Get Upcoming History
        """

        # Get all user book histories
        histories = Book.query.filter_by(UserId=userId).all()

        # If not booked yet
        if not histories:
            return {"message": "You have not Booked Yet"}, 404

        # upcoming list
        upcoming = []
        # # Check DateTime and if greater add to upcoming list
        for history in histories:
            tour = Tours.query.filter_by(TourId=history.TourId).first()

            date = datetime.strptime(tour.StartingDate, "%Y-%m-%d %H:%M:%S.%f")
            if date >= datetime.now():
                # Get Tour Details from Database
                upcoming.append(tour)

        # for history in histories:
        #     tour = Tours.query.filter_by(TourId=history.TourId).all()
        if not upcoming:
            return {"message": "No Past Histories"}, 404
        return tours_schema.dump(upcoming)


@namespace3.route("/<int:userId>/history/past")
class UserPastHistoriesResource(Resource):
    def get(self, userId):
        """
        Get Past History
        """
        # Get all user book histories
        histories = Book.query.filter_by(UserId=userId).all()

        # If not booked yet
        if not histories:
            return {"message": "You have not Booked Yet"}, 404

        # past list
        past = []
        # Check DateTime and if less, add to past list
        for history in histories:
            tour = Tours.query.filter_by(TourId=history.TourId).first()

            date = datetime.strptime(tour.StartingDate, "%Y-%m-%d %H:%M:%S.%f")
            if date < datetime.now():
                # Get Tour Details from Database
                past.append(tour)
        if not past:
            return {"message": "No Past Histories"}, 404

        return tours_schema.dump(past)







   



     
  
       
        

       
        

        
        
           
       
        
            

     
        



    

       

        
        


    
            
            
           
