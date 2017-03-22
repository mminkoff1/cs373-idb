from flask import Flask, render_template
import os
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

db = SQLAlchemy(app)

class Game(db.Model):
	__tablename__ = 'game'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	publisher = Column(String)
	num_players = Column(Integer)
	avg_score = Column(Integer)
	systems = Column(String)
	theme = Column(String)


class Publisher(db.Model):
	__tablename__ = 'publisher'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	num_games = Column(Integer)
	year_founded = Column(Integer)
	country = Column(String)
	num_franchises = Column(Integer)


class Genre(db.Model):
	__tablename__ = 'genre'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	num_games = Column(Integer)
	avg_rating = Column(Integer)
	rel_genre = Column(String)
	popularity = Column(Integer)


@app.route('/')
def splash():
	return render_template("splash.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/games')
def games():
	return render_template("games.html",  games=Game.query.all(), publishers=Publisher.query.all())

@app.route('/genre')
def genre():
	return render_template("genre.html")

@app.route('/publisher')
def publisher():
	return render_template("publisher.html")

if __name__ == "__main__":

	db.create_all()				# Only want to do this once, this is just here for demonstration
	
	game = Game()
	game.name = "The Witcher 3"
	game.year = 2015
	game.theme = "Action RPG"
	game.publisher = "CD Projekt RED"

	publisher = Publisher()
	publisher.name = "CD Projekt RED"
	publisher.country = "Poland"
	publisher.year = 1994
	publisher.num_franchises = 1

	db.session.add(game)
	db.session.add(publisher)
	db.session.commit()

	app.run()
