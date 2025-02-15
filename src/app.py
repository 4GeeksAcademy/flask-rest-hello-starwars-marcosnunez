"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person
from models import db, User, Favourite, Character, Starships, Planets
from enum import Enum

class FavoriteTypeEnum(str, Enum):
    Planets = "Planet"
    Character = "Character"
    Starships = "Starship"


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/characters", methods=["GET"])
def get_characters():
    characters = Character.query.all()
    return jsonify(characters), 200

@app.route("/characters/<int:character_id>",methods=["GET"])
def get_character(character_id):
    character = Character.query.get(character_id)
    return jsonify(character) if character else (jsonify({"error" : "character not found"}), 404)

@app.route("/planets", methods=["GET"])
def get_planets():
    planets = Planets.query.all()
    return jsonify(planets), 200

@app.route("/planets/<int:planets_id>",methods=["GET"])
def get_planet(planets_id):
    planet = Planets.query.get(planets_id)
    return jsonify(planet) if planet else (jsonify({"error" : "planet not found"}), 404)

@app.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users), 200

@app.route("/planets/<int:user_id>",methods=["GET"])
def get_user(user_id):
    user = Planets.query.get(user_id)
    return jsonify(user) if user else (jsonify({"error" : "user not found"}), 404)

@app.route('/starships', methods=["GET"])
def get_starships():
    starships = Starships.query.all()
    return jsonify(starships), 200

@app.route("/planets/<int:starship_id>",methods=["GET"])
def get_starship(starship_id):
    starship = Starships.query.get(starship_id)
    return jsonify(starship) if starship else (jsonify({"error" : "user not found"}), 404)

class FavoriteTypeEnum(str, Enum):
    Planets = "Planet"
    Character = "Character"
    Starships = "Starship"

@app.route("/users/favorites", methods=["GET"])
def get_user_favorites():
    user_id = request.args.get("user_id")  
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    favorites = Favourite.query.filter_by(user_id=user_id).all()
    return jsonify(favorites), 200

@app.route("/favorite/planet/<int:planet_id>", methods=["POST"])
def add_favorite_planet(planet_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    planet = Planets.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    
    new_favorite = Favourite(
        external_id=planet_id, 
        type=FavoriteTypeEnum.Planets, 
        name=planet.name, 
        user_id=user_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"message": "Favorite planet added successfully"}), 201

@app.route("/favorite/character/<int:character_id>", methods=["POST"])
def add_favorite_character(character_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "Character not found"}), 404
    
    new_favorite = Favourite(
        external_id=character_id, 
        type=FavoriteTypeEnum.Character, 
        name=character.name, 
        user_id=user_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"message": "Favorite character added successfully"}), 201

@app.route("/favorite/starship/<int:starship_id>", methods=["POST"])
def add_favorite_starship(starship_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    starship = Starships.query.get(starship_id)
    if not starship:
        return jsonify({"error": "Starship not found"}), 404
    
    new_favorite = Favourite(
        external_id=starship_id, 
        type=FavoriteTypeEnum.Starships, 
        name=starship.name,
        user_id=user_id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({"message": "Favorite starship added successfully"}), 201

@app.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
def delete_favorite_planet(planet_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    favorite = Favourite.query.filter_by(
        external_id=planet_id, 
        user_id=user_id, 
        type=FavoriteTypeEnum.Planets).first()
    if not favorite:
        return jsonify({"error": "Favorite planet not found"}), 404
    
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite planet deleted successfully"}), 200

@app.route("/favorite/character/<int:character_id>", methods=["DELETE"])
def delete_favorite_character(character_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    favorite = Favourite.query.filter_by(external_id=character_id, user_id=user_id, type=FavoriteTypeEnum.Character).first()
    if not favorite:
        return jsonify({"error": "Favorite character not found"}), 404
    
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite character deleted successfully"}), 200

@app.route("/favorite/starship/<int:starship_id>", methods=["DELETE"])
def delete_favorite_starship(starship_id):
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    favorite = Favourite.query.filter_by(external_id=starship_id, user_id=user_id, type=FavoriteTypeEnum.Starships).first()
    if not favorite:
        return jsonify({"error": "Favorite starship not found"}), 404
    
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"message": "Favorite starship deleted successfully"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
