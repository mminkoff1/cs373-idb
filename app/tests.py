from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Publisher, Character
#from populate1 import engine

class TestModels (TestCase):
    def setUp(self):
	self.engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + 
                               "@" + "35.184.159.10" + "/" + "gamelookup")
	self.sess = sessionmaker(bind = self.engine)

    def test_game_1(self):
        session = self.sess()
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.name, "Game")
        session.delete(result)
	session.commit()

    def test_game_2(self):
	session = self.sess()
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.year, 2017)
        session.delete(result)
	session.commit()

    def test_game_3(self):
	session = self.sess()
        game = Game(ident = 99999, name = "Game", year = 2017, 
                    publisher = "Lookup Games", avg_score = 'E', 
                    theme = "Fun")
        session.add(game)
        session.commit()
        result = session.query(Game).get(99999)
        self.assertEqual(result.publisher, "Lookup Games")
        session.delete(result)
	session.commit()

    def test_publisher_1(self):
        session = self.sess()
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.name, "Publisher")
        session.delete(result)
	session.commit()

    def test_publisher_2(self):
        session = self.sess()
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.num_games, 3)
        session.delete(result)
	session.commit()

    def test_publisher_3(self):
        session = self.sess()
        publisher = Publisher(ident = 99999, name = "Publisher", 
                              num_games = 3, year_founded = 2000, 
                              country = "England", website = "Fake.com")
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).get(99999)
        self.assertEqual(result.year_founded, 2000)
        session.delete(result)
	session.commit()

    def test_character_1(self):
        session = self.sess()
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.name, "Fares Fraij")
        session.delete(result)
	session.commit()

    def test_character_2(self):
        session = self.sess()
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.gender, "Male")
        session.delete(result)
	session.commit()
        
    def test_character_3(self):
        session = self.sess()
        character = Character(ident = 99999, name = "Fares Fraij", 
                              gender = "Male", franchise = "UT", 
                              location = "GDC", first_game = "SWE")
        session.add(character)
        session.commit()
        result = session.query(Character).get(99999)
        self.assertEqual(result.location, "GDC")
        session.delete(result)
	session.commit()
        
if __name__ == "__main__":  
    main()
