from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Game(Base):
	__tablename__ = 'game'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(Integer)
	publisher = Column(String)
	num_players = Column(Integer)
	avg_score = Column(Integer)
	systems = Column(String)
	theme = Column(String)

	#Relationships
    publisher = relationship("Publisher", back_populates="game")
    genre = relationship("Genre", back_populates="game")
	

class Publisher(Base):
	__tablename__ = 'publisher'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	num_games = Column(Integer)
	year_founded = Column(Integer)
	country = Column(String)
	num_franchises = Column(Integer)


	#Relationships

    game = relationship("Game", back_populates="publisher")
    genre = relationship("Genre", back_populates="publisher")


class Genre(Base):
	__tablename__ = 'genre'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	num_games = Column(Integer)
	avg_rating = Column(Integer)
	rel_genre = Column(String)
	popularity = Column(Integer)


	#Relationships
	publisher_id = Column(Integer, ForeignKey('publisher.id')) 

    publisher = relationship("Publisher", back_populates="genre")
    game = relationship("Game", back_populates="genre")
    


if __name__ == '__main__':
	engine =  create_engine("")
	Base.metadata.create_all(engine)

