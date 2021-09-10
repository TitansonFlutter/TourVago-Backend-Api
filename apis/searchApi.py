# Import modules
from flask_restplus import Resource, Namespace, fields
from flask import request, Flask
from sqlalchemy import or_

from Model.models import *
from marsh import *
from .agentApi import tours_schema, tour_schema

# Instance app
app = Flask(__name__)

# Filter Namespace
namespace5 = Namespace("filters", description="Filter related operations")

filter = namespace5.model(
    "Filter",
    {
        "priceLow": fields.Float,
        "priceHigh": fields.Float,
        "tourName": fields.String,
    },
)

# Search Api
@namespace5.route("")
class FiltersResource(Resource):
    @namespace5.expect(filter)
    def post(self):
        """
        Filter Tours
        """

        print(request.json["tourName"])
        print(request.json["priceLow"])
        print(request.json["priceHigh"])
        result = 0
        if request.json["tourName"] and request.json["priceLow"]:
            print("////////////////////////////////////a")
            result = Tours.query.filter(
                Tours.Price <= request.json["priceHigh"],
                Tours.Price >= request.json["priceLow"],
                Tours.TourName == request.json["tourName"],
            ).all()
        elif request.json["tourName"] and not request.json["priceLow"]:
            print("////////////////////////////////////b")

            result = Tours.query.filter(
                Tours.TourName == request.json["tourName"]
            ).all()
        elif not request.json["tourName"] and request.json["priceLow"]:
            print("////////////////////////////////////c")

            result = Tours.query.filter(
                Tours.Price <= request.json["priceHigh"],
                Tours.Price >= request.json["priceLow"],
            ).all()
        print(result)
        if result != 0:
            ans = []
            for item in result:
                tourAgent = Users.query.filter_by(UserId=item.UserId).first()
                total = 0
                count = 0
                tourId = item.TourId
                reviews = Review.query.filter_by(TourId=tourId).all()
                if reviews:
                    for review in reviews:
                        total += review.Rate
                        count += 1
                if count > 0:
                    temp = {
                        "TourId": item.TourId,
                        "Price": item.Price,
                        "TourName": item.TourName,
                        "TourImage": item.TourImage,
                        "TourAgent": tourAgent.UserName,
                        "Rating": total / count,
                        "Country": item.Country,
                        "Region": item.Region,
                        "City": item.City,
                        "WhatIsIncluded": item.WhatIsIncluded,
                        "WhatIsExcluded": item.WhatIsIncluded,
                        "TourDescription": item.TourDescription,
                        "WhatToBring": item.WhatToBring,
                        "Itinerary": item.Itinerary,
                        "Duration": item.Duration,
                        "StartingDate": item.StartingDate,
                        # "Special": item.Special,
                        "Updated": item.Updated,
                    }
                else:
                    temp = {
                        "Price": item.Price,
                        "TourName": item.TourName,
                        "TourImage": item.TourImage,
                        "TourAgent": tourAgent.UserName,
                        "Rating": 0,
                        "Country": item.Country,
                        "Region": item.Region,
                        "City": item.City,
                        "WhatIsIncluded": item.WhatIsIncluded,
                        "WhatIsExcluded": item.WhatIsIncluded,
                        "TourDescription": item.TourDescription,
                        "WhatToBring": item.WhatToBring,
                        "Itinerary": item.Itinerary,
                        "Duration": item.Duration,
                        "StartingDate": item.StartingDate,
                        # "Special": item.Special,
                        "Updated": item.Updated,
                    }
                ans.append(temp)
            print(ans)
            return ans, 200

        return {"message": "No Result"}, 404
@namespace5.route("/<string:name>")
class FilterResource(Resource):
    def get(self, name):
        name = name

        res = Tours.query.filter(
            or_(
                Tours.TourName.like(f"%{name}%"),
                Tours.TourDescription.like(f"%{name}%"),
                Tours.WhatIsExcluded.like(f"%{name}%"),
                Tours.Country.like(f"%{name}%"),
                Tours.City.like(f"%{name}%"),
                Tours.Itinerary.like(f"%{name}%"),
                Tours.WhatIsIncluded.like(f"%{name}%"),
                Tours.WhatToBring.like(f"%{name}%"),
                Tours.Region.like(f"%{name}%"),
            )
        ).all()

        if not res:
            return {"message": "No Tours Available"}, 404

        return tours_schema.dump(res)

