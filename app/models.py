from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask import Flask

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:seanpickupyourphone@/35.184.159.10?host=/gamelookup'


app.config[
    'SQLALCHEMY_DATABASE_URI'] =                                    \
    'postgres://postgres:seanpickupyourphone@35.184.159.10/gamelookup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:seanpickupyourphone@/35.184.159.10/gamelookup?host=/cloudsql/game-lookup:us-central1:gamelookup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Game(db.Model):
	__tablename__ = 'games'

	ident = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	year = db.Column(db.Integer)
	publisher = db.Column(db.String())
	#num_players = db.Column(Integer)
	#notable_char
	avg_score = db.Column(db.String())
	#systems = db.Column(db.String())
	theme = db.Column(db.String())
	picture = db.Column(db.String())
	description = db.Column(db.String())
	characterid = db.Column(db.String())
	#what print will return	
	def __repr__(self):
		return  "<Game(name='%s', year='%s', publisher='%s', avg_score='%s', theme='%s')>" % (
				self.name, self.year, self.publisher, self.avg_score, self.theme)

	@property
	def serialize(self):
		return {
			'ident' : self.ident,
			'name' : self.name,
			'year' : self.year,
			'publisher' : self.publisher,
			'avg_score' : self.avg_score,
			'theme' : self.theme,
			'picture' : self.picture,
			'description' : self.description,
			'characterid' : self.characterid
		}


class Publisher(db.Model):
	__tablename__ = 'publishers'

	def __init__(self, ident, name, num_games, year_founded, country, website):
	    self.ident = ident
	    self.name = name
	    self.num_games = int(num_games)
	    self.year_founded = year_founded
	    self.country = country
	    self.website = website


	ident = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	#abbreviation = db.Model(db.String())

	num_games = db.Column(db.Integer)
	year_founded = db.Column(db.Integer)
	country = db.Column(db.String())
	#num_franchises = db.Column(Integer)
	#notable_games
	website = db.Column(db.String())
	picture = db.Column(db.String())

	@property
	def serialize(self): 
		return {
			'ident' : self.ident,
			'name' : self.name,
			'num_games' : self.num_games,
			'year_founded' : self.year_founded,
			'country' : self.country,
			'website' : self.website,
			'picture' : self.picture
		}


class Character(db.Model):
	__tablename__ = 'characters'

	def __init__(self, ident, name, gender, franchise, location, first_game):
	    self.ident = ident
	    self.name = name
	    self.gender = gender
	    self.franchise = franchise
	    self.location = location
	    self.first_game = first_game

	ident = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String())
	gender = db.Column(db.String())
	franchise = db.Column(db.String())
	location = db.Column(db.String())
	first_game = db.Column(db.String())
	publid = db.Column(Integer)
	picture = db.Column(db.String())

	@property
	def serialize(self): 
		return {
			'ident' : self.ident,
			'name' : self.name,
			'gender' : self.gender,
			'franchise' : self.franchise,
			'location' : self.location,
			'first_game' : self.first_game,
			'picture' : self.picture,
			'publid' : self.publid
		}

"""
if __name__ == '__main__':
	engine =  create_engine("")
	Base.metadata.create_all(engine)
"""

