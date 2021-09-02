from flask import Flask
from settings import *
from Model.models import *

app = Flask(__name__)

app.config["SERVER_NAME"] = FLASK_SERVER_NAME
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
# app.config["WHOOSH_BASE"] = "whoosh"

db.init_app(app)


def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
