from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    UserId = db.Column(db.Integer, primary_key=True)
    Role = db.Column(db.String, nullable=False)
    UserName = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, unique=True, nullable=False)
    Password = db.Column(db.String, nullable=False)


class AgentInfo(db.Model):
    __tablename__ = "agentInfo"
    AgentInfoId = db.Column(db.Integer, primary_key=True)
    AgentId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)
    Approved = db.Column(db.Boolean, nullable=False)
    Acronyms = db.Column(db.String, nullable=False)
    Motto = db.Column(db.String, nullable=False)
    Description = db.Column(db.String, nullable=False)
    Website = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)

class Book(db.Model):
    __tablename__ = "book"
    BookId = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)
    TourId = db.Column(db.Integer, db.ForeignKey("Tours.ToursId"), nullable=False)

class History(db.Model):
    __tablename__ = "history"
    HistoryId = db.Column(db.Integer, primary_key=True)
    AgentName = db.Column(db.String, nullable=False)
    PlaceName = db.Column(db.String, nullable=False)
    Rate = db.Column(db.String, nullable=False)
    Date = db.Column(db.String, nullable=False)
    ShortDescription = db.Column(db.String, nullable=False)
    UserId = db.Column(db.Integer, db.ForeignKey("Users.UserId"), nullable=False)


