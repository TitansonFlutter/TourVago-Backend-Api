# Import modules
from flask_restplus import Resource, Namespace
from flask import Flask

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
