from unittest import main, TestCase
from sqlalchemy.orm import sessionmaker
from models import Game, Publisher, Character
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask import Flask
'''
class TestModels (TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.config[
            'SQLALCHEMY_DATABASE_URI'] =                                    \
            'postgres://postgres:seanpickupyourphone@35.184.159.10/gamelookup'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = SQLAlchemy(app)

    def test_game_1(self):
        #session = self.sess()
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session = self.db.session
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.name, "Game")
        session.delete(result)
        session.commit()

    def test_game_2(self):
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session = self.db.session
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.year, 2017)
        session.delete(result)
	session.commit()

    def test_game_3(self):
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session = self.db.session
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.publisher, "Lookup Games")
        session.delete(result)
	session.commit()

    def test_publisher_1(self):
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session = self.db.session
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.name, "Publisher")
        session.delete(result)
	session.commit()

    def test_publisher_2(self):
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session = self.db.session
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.num_games, 3)
        session.delete(result)
	session.commit()

    def test_publisher_3(self):
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session = self.db.session
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.year_founded, 2000)
        session.delete(result)
	session.commit()

    def test_character_1(self):
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session = self.db.session
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.name, "Fares Fraij")
        session.delete(result)
	session.commit()

    def test_character_2(self):
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session = self.db.session
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.gender, "Male")
        session.delete(result)
	session.commit()
        
    def test_character_3(self):
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session = self.db.session
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.location, "GDC")
        session.delete(result)
	session.commit()
        
if __name__ == "__main__":  
    main()
'''