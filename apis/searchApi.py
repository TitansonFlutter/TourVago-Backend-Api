# Import modules
from flask_restplus import Resource, Namespace
from flask import request, Flask

from Model.models import *
from marsh import *


# Instance app
app = Flask(__name__)

# Filter Namespace
namespace5 = Namespace("filters", description="Filter related operations")


# Search Api
@namespace5.route("")
class FiltersResource(Resource):
    def post(self):
        """
        Filter Tours
        """
        result = ""
        if(request.json['query']):
            result = Tours.query.whoosh_search(request.json['query']).all()

        if (result):
            if(request.json['tourName'] and request.json['priceLow']):
                result.filter(Tours.Price <= request.json['priceHigh'], Tours.Price >= request.json['priceLow'],Tours.TourName == request.json['tourName']).all()
            if(request.json['tourName'] and not request.json['priceLow']):
                result.filter(Tours.TourName == request.json['tourName']).all()
            if(not request.json['tourName'] and request.json['priceLow']):
                result.filter(Tours.Price <= request.json['priceHigh'], Tours.Price >= request.json['priceLow']).all()
        else:
            if(request.json['tourName'] and request.json['priceLow']):
                result = Tours.query.filter(Tours.Price <= request.json['priceHigh'], Tours.Price >= request.json['priceLow'],Tours.TourName == request.json['tourName']).all()
            if(request.json['tourName'] and not request.json['priceLow']):
                result = Tours.query.filter(Tours.TourName == request.json['tourName']).all()
            if(not request.json['tourName'] and request.json['priceLow']):
                result = Tours.query.filter(Tours.Price <= request.json['priceHigh'], Tours.Price >= request.json['priceLow']).all()
        if result:
            ans = []
            for item in result:
                tourAgent = Users.query.filter_by(UserId=item.UserId).first()
                total = 0
                count = 0
                tourId = item.TourId
                reviews = Reviews.query.filter_by(TourId=tourId).all()
                for review in reviews:
                    total += review.Rate
                    count += 1
                temp = {"TourName" : item.TourName,"TourImage" : item.TourImage,"TourAgent" : tourAgent.UserName,"Rating" : total / count}
                ans.append(temp)

            return ans,200
            
        return 404 



        
        
