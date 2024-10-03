# app/models.py

from app import db
from flask_login import UserMixin

class HousingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    distance_to_college = db.Column(db.Float)
    popularity = db.Column(db.Integer)
    user_rating = db.Column(db.Float)
    # Additional fields as needed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'address': self.address,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'distance_to_college': self.distance_to_college,
            'popularity': self.popularity,
            'user_rating': self.user_rating,
            # Include additional fields as needed
        }

    def __repr__(self):
        return f'<HousingOption {self.title}>'

# Example User and Rating models for authentication and ratings

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # Relationships
    ratings = db.relationship('Rating', back_populates='user')

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    housing_option_id = db.Column(db.Integer, db.ForeignKey('housing_option.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.Text)
    # Relationships
    housing_option = db.relationship('HousingOption', back_populates='ratings')
    user = db.relationship('User', back_populates='ratings')
