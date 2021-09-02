from flask_sqlalchemy import SQLAlchemy

# import flask_whooshalchemy as wa
db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    UserId = db.Column(db.Integer, primary_key=True)
    Role = db.Column(db.Integer, nullable=False)
    UserName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, unique=True, nullable=False)
    Password = db.Column(db.String, nullable=False)


class AgentInfo(db.Model):
    __tablename__ = "agentInfo"
    AgentInfoId = db.Column(db.Integer, primary_key=True)
    AgentId = db.Column(db.Integer, db.ForeignKey("users.UserId"), nullable=False)
    Approved = db.Column(db.Boolean, nullable=False)
    Acronym = db.Column(db.String, nullable=False)
    Motto = db.Column(db.String, nullable=False)
    Description = db.Column(db.String, nullable=False)
    Website = db.Column(db.String, nullable=False)
    Country = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)
    City = db.Column(db.String, nullable=False)
    Address = db.Column(db.String, nullable=False)
    PhoneNumber = db.Column(db.String, nullable=False)
    ZipCode = db.Column(db.String, nullable=False)


class Book(db.Model):
    __tablename__ = "book"
    BookId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey("users.UserId"), nullable=False)
    TourId = db.Column(db.Integer, db.ForeignKey("tours.TourId"), nullable=False)


class Review(db.Model):
    __tablename__ = "review"
    ReviewId = db.Column(db.Integer, primary_key=True)
    Comment = db.Column(db.String, nullable=False)
    Rate = db.Column(db.String, nullable=False)
    Date = db.Column(db.String, nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey("users.UserId"), nullable=False)
    TourId = db.Column(db.Integer, db.ForeignKey("tours.TourId"), nullable=False)


class Tours(db.Model):
    _searchable__ = [
        "TourName",
        "Country",
        "Region",
        "City",
        "WhatIsIncluded",
        "WhatIsExcluded",
        "TourDescription",
        "WhatToBring",
        "Itinerary",
        "Duration",
        "StartingDate",
        "Price",
        "Updated",
    ]
    __tablename__ = "tours"
    TourId = db.Column(db.Integer, primary_key=True)
    TourName = db.Column(db.String, nullable=False)
    TourImage = db.Column(db.String, nullable=False)
    Country = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)
    City = db.Column(db.String, nullable=False)
    WhatIsIncluded = db.Column(db.String, nullable=False)
    WhatIsExcluded = db.Column(db.String, nullable=False)
    TourDescription = db.Column(db.String, nullable=False)
    WhatToBring = db.Column(db.String, nullable=False)
    Itinerary = db.Column(db.String, nullable=False)
    Duration = db.Column(db.String, nullable=False)
    StartingDate = db.Column(db.String, nullable=False)
    Price = db.Column(db.String, nullable=False)
    Updated = db.Column(db.Boolean, nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey("users.UserId"), nullable=False)


# wa.whoosh_index(app,Tours)
