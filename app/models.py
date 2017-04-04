from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
	__tablename__ = 'games'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	publisher = Column(String)
	#num_players = Column(Integer)
	avg_score = Column(Integer)
	#systems = Column(String)
	theme = Column(String)


class Publisher(Base):
	__tablename__ = 'publishers'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	num_games = Column(Integer)
	year_founded = Column(Integer)
	country = Column(String)
	#num_franchises = Column(Integer)


class Character(Base):
	__tablename__ = 'characters'

	id = Column(Integer, primary_key=True)
	name = Column(String)
        gender = Column(Integer)
        species = Column(Integer)
        num_games = Column(Integer)

"""
if __name__ == '__main__':
	engine =  create_engine("")
	Base.metadata.create_all(engine)
"""
