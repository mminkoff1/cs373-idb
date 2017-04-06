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


class Character(Base):
	__tablename__ = 'characters'

	ident = Column(Integer, primary_key=True)
	name = Column(String)
        gender = Column(String)
        species = Column(String)
        num_games = Column(Integer)
        first_game = Column(String)

"""
if __name__ == '__main__':
	engine =  create_engine("")
	Base.metadata.create_all(engine)
"""
