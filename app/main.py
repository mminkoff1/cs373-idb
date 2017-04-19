import sys, traceback
sys.path.insert(0, './app/')
import tests

from flask import Flask, render_template, jsonify, request
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Game, Publisher, Character, app
import os
import subprocess

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
	game = Game.query.filter(Game.ident == game_id).first()
	character = Character.query.filter(Character.ident == game.characterid).first()
	publisher = Publisher.query.filter(Publisher.name == game.publisher).first()
	return render_template("game.html", game = game, character = character, publisher = publisher)

@app.route('/publishers/<int:publisher_id>')
def get_publisher(publisher_id):
	publisher = Publisher.query.filter(Publisher.ident == publisher_id).first()
	character = Character.query.filter(Character.ident == publisher.characterid).first()
	game = Game.query.filter(Game.ident == publisher.gameid).first()
	return render_template("publisher.html", game = game, character = character, publisher = publisher)

@app.route('/characters/<int:character_id>')
def get_character(character_id):
	character = Character.query.filter(Character.ident == character_id).first()
	publisher = Publisher.query.filter(Publisher.ident == character.publid).first()
	game = Game.query.filter(Game.name == character.first_game).first()
	return render_template("character.html", game = game, character = character, publisher = publisher)



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

#Taken from Sethalopod github
@app.route('/test/')
def test():
    script_dir = os.path.dirname(__file__)
    rel_path = "tests.py"
    try:
    	process = subprocess.check_output(["python", os.path.join(script_dir, rel_path)],
    		stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
    	process = e.output

    result = process.decode("utf-8")
    result = result.replace('-', '')

    return result      


if __name__ == "__main__":
	app.run()
