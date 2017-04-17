
import sys, traceback
sys.path.insert(0, './app/')

from flask import Flask, render_template, jsonify, request
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Game, Publisher, Character, app
      


'''
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'
app.config.from_object(__name__) # load config from this file , flaskr.py

#connect to database
engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")

Session = sessionmaker(bind = engine)
session = Session()
'''

@app.route('/')
def splash():
	return render_template("splash.html")

@app.route('/about/')
def about():
	return render_template("about.html")

@app.route('/games/')
def games():
	try:
		data = Game.query.all()
		return render_template("games.html",
			games = data)
	except:
		data = "Failed :("
		return (data)

@app.route('/publishers/')
def publishers():
	return render_template("publishers.html",
		publishers = Publisher.query.all())

@app.route('/characters/')
def characters():
	return render_template("characters.html",
		characters = Character.query.all())



@app.route('/games/<int:game_id>')
def get_game(game_id):
	game = Game.query.filter(Game.ident == game_id)
	character = Character.query.filter(characterid == Character.ident)
	publisher = Publisher.query.filter(publisher == Publisher.name)
	return render_template("game.html", game = game, character = character, publisher = publisher)

@app.route('/publishers/<int:publisher_id>')
def get_publisher(publisher_id):
	publisher = Publisher.query.filter(Publisher.ident == publisher_id)
	return render_template("publisher.html", publisher = publisher)

@app.route('/characters/<int:character_id>')
def get_character(character_id):
	character = Character.query.filter(Character.ident == character_id)
	return render_template("character.html", character = character)



@app.route('/api/games/')
def gamedata():
	try:
		data = Game.query.all()
		return jsonify(games_list=[i.serialize for i in data])
	except:
		data = "Failed :("
		return data

@app.route('/api/games/<int:game_id>/')
def get_game_id(game_id):
	game = Game.query.filter(Game.ident == game_id).first()
	game = game.__dict__.copy()
	game.pop('_sa_instance_state', None)
	return jsonify(game)


@app.route('/api/publishers/')
def publisherdata():
	try:
		data = Publisher.query.all()
		return jsonify(publishers_list=[i.serialize for i in data])
	except:
		data = "Failed :("
		return data

@app.route('/api/publishers/<int:publisher_id>/')
def get_publisher_id(publisher_id):
	publisher = Publisher.query.filter(Publisher.ident == publisher_id).first()
	publisher = publisher.__dict__.copy()
	publisher.pop('_sa_instance_state', None)
	return jsonify(publisher)


@app.route('/api/characters/')
def characterdata():
	try:
		data = Character.query.all()
		return jsonify(characters_list=[i.serialize for i in data])
	except:
		data = "Failed :("
		return data

@app.route('/api/characters/<int:character_id>/')
def get_character_id(character_id):
	character = Character.query.filter(Character.ident==character_id).first()
	character = character.__dict__.copy()
	character.pop('_sa_instance_state', None)
	return jsonify(character)


if __name__ == "__main__":
	app.run()
