from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import db


# db = SQLAlchemy()




class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))   
    genres = db.Column(ARRAY(String))
    # genres = db.Column(db.Enum(String(120)))
    image_link = db.Column(db.String(500))  
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref="Venue", lazy=True)
    def __init__(self, name, city, state,address,phone,genres,image_link,facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.genres = genres
        self.image_link = image_link
        self.facebook_link = facebook_link

    def insert(self):
        db.session.add(self)
        db.session.commit()

    # def update(self):
    #     db.session.commit()
    
    # def delete(self):
    #     db.session.delete(self)
    #     db.session.commit()
       
    # def __repr__(self):
    #     return '<id {}>'.format(self.id) 
    #   def insert(self):
    #       db.session.add(self)
    #       db.session.commit()

    #   def update(self):
    #       db.session.commit()
    
    #   def delete(self):
    #       db.session.delete(self)
    #       db.session.commit()


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref="Artist", lazy=True)

    def __init__(self, name, city, state,address,phone,genres,image_link,facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.genres = genres
        self.image_link = image_link
        self.facebook_link = facebook_link

    # def __repr__(self):
    #     return '<id {}>'.format(self.id) 
        

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
   

# show table
class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey(
        'Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, artist_id, venue_id,start_time):
      self.id = id
      self.artist_id = artist_id
      self.venue_id = venue_id
      self.start_time = start_time
     
    # def __repr__(self):
    #     return '<Show {}{}>'.format(self.artist_id, self.venue_id)

    # def __repr__(self):
    #     return '<id {}>'.format(self.id) 

    def insert(self):
        db.session.add(self)
        db.session.commit()
