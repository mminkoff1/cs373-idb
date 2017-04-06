from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
	__tablename__ = 'games'

	ident = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	publisher = Column(String)
	#num_players = Column(Integer)

	#notable_char
	avg_score = Column(String)
	#systems = Column(String)
	theme = Column(String)

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
			'theme' : self.theme
		}


class Publisher(Base):
	__tablename__ = 'publishers'

	def __init__(self, ident, name, num_games, year_founded, country, website):
	    self.ident = ident
	    self.name = name
	    self.num_games = int(num_games)
	    self.year_founded = year_founded
	    self.country = country
	    self.website = website


	ident = Column(Integer, primary_key=True)
	name = Column(String)
	#abbreviation = Column(String)

	num_games = Column(Integer)
	year_founded = Column(Integer)
	country = Column(String)
	#num_franchises = Column(Integer)
	#notable_games
	website = Column(String)

	#what print will return	
	def __repr__(self):
		return  "<Publisher(name='%s', num_games='%s', year_founded='%s', country='%s', website='%s')>" % (
				self.name, self.num_games, self.year_founded, self.country, self.website)

	@property
	def serialize(self): 
		return {
			'ident' : self.ident,
			'name' : self.name,
			'num_games' : self.num_games,
			'year_founded' : self.year_founded,
			'country' : self.country,
			'website' : self.website
		}


class Character(Base):
	__tablename__ = 'characters'

	def __init__(self, ident, name, gender, franchise, location, first_game):
	    self.ident = ident
	    self.name = name
	    self.gender = gender
	    self.franchise = franchise
	    self.location = location
	    self.first_game = first_game

	ident = Column(Integer, primary_key=True)
	name = Column(String)
  gender = Column(String)
  franchise = Column(String)
  location = Column(String)
  first_game = Column(String)

	@property
	def serialize(self): 
		return {
			'ident' : self.ident,
			'name' : self.name,
			'gender' : self.gender,
			'franchise' : self.franchise,
			'location' : self.location,
			'first_game' : self.first_game
		}

"""
if __name__ == '__main__':
	engine =  create_engine("")
	Base.metadata.create_all(engine)
"""