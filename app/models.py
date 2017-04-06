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
	picture = Column(String)
	description = Column(String)
	characterid = Column(String)
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


class Publisher(Base):
	__tablename__ = 'publishers'

	ident = Column(Integer, primary_key=True)
	name = Column(String)
	#abbreviation = Column(String)

	num_games = Column(Integer)
	year_founded = Column(Integer)
	country = Column(String)
	#num_franchises = Column(Integer)
	#notable_games
	website = Column(String)
	picture = Columnt(String)

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
			'website' : self.website,
			'picture' : self.picture
		}


class Character(Base):
	__tablename__ = 'characters'

	ident = Column(Integer, primary_key=True)
	name = Column(String)
	gender = Column(String)
	franchise = Column(String)
	location = Column(Integer)
	first_game = Column(String)
	publid = Column(Integer)
	picture = Column(String)

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