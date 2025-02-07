from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy import ForeignKey
db = SQLAlchemy()
from enum import Enum
@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id:int = db.Column(db.Integer, primary_key=True, nullable = False)
    user_name:str = db.Column(db.String(50), nullable = False)
    password:str = db.Column(db.VARCHAR(60), nullable = False)
    email:str = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return '<User %r>' % self.user
    
class FavoriteTypeEnum(str, Enum):
    Planets= "Planet"
    Character = "Character"
    Starships = "Starship"

@dataclass
class Favourite(db.Model):
    __tablename__ = 'favourite'
    id:int = db.Column(db.Integer, primary_key=True, nullable = False)
    external_id:int = db.Column(db.Integer, nullable = False)
    type:FavoriteTypeEnum = db.Column(db.Enum(FavoriteTypeEnum), nullable = False, unique = True)
    name:str = db.Column(db.String(50), nullable = False)
    user_id:int = db.Column(db.Integer, ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return '<Favourite %r>' % self.favourite
@dataclass
class Character(db.Model):
    __tablename__ = 'character'
    id:int = db.Column(db.Integer, primary_key=True, nullable = False)
    name:str = db.Column(db.String(50), nullable=False)
    height:int = db.Column(db.Integer, nullable=False)
    home_world:str = db.Column(db.Integer,ForeignKey('planets.id'), nullable = False)
    mass:int= db.Column(db.Integer, nullable = False)
    hair_color:str= db.Column(db.String(50), nullable=False)
    eye_color:str=  db.Column(db.String(50), nullable = False)
    birth_year:int = db.Column(db.Integer, nullable=False)
    gender:int = db.Column(db.Integer, nullable=False)
    description:str = db.Column(db.String(5000), nullable=False)
    def __repr__(self):
        return '<Character %r>' % self.character
@dataclass
class Starships(db.Model):
    _tablename_= 'starships'
    id:int = db.Column(db.Integer, primary_key=True, nullable = False)
    name:str = db.Column(db.String(50), nullable=False)
    cargo_capacity:int = db.Column(db.Integer, nullable=False)
    mlgt:str = db.Column(db.String(50), nullable=False)
    consumables:str = db.Column(db.String(50), nullable=False)
    cost_in_credits:int = db.Column(db.Integer, nullable=False)
    crew:str = db.Column(db.String(5000), nullable=False)
    hyperdrive_rating:int = db.Column(db.Integer, nullable=False)
    length:int  = db.Column(db.Integer,nullable=False)
    manufacturer:int = db.Column(db.Integer, nullable=False)
    passengers:str = db.Column(db.String(5000), nullable=False)
    model:str = db.Column(db.String(5000), nullable=False)
    max_atmosphering_speed:int =  db.Column(db.Integer, nullable=False)
    starship_class:str = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return '<Starships %r>' % self.starships

@dataclass
class Planets(db.Model):
    _tablename_ = 'planets'
    id:int = db.Column(db.Integer, primary_key=True, nullable = False)
    name:str = db.Column(db.String(50), nullable=False)
    climate:str =  db.Column(db.String(50), nullable=False)
    diameter:int  = db.Column(db.Integer, nullable=False)
    gravity:int  = db.Column(db.Integer, nullable=False)
    orbital_period:int  = db.Column(db.Integer, nullable=False)
    population:int  = db.Column(db.Integer, nullable=False)
    rotation_period:int  = db.Column(db.Integer, nullable=False)
    terrain:str =  db.Column(db.String(50), nullable=False)
    surface_water:int  = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Planets %r>' % self.planets