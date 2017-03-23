from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, Cuisine
from config import test_db

class TestModels (TestCase):

    def test_game_1(self):
        session = self.sess()
        game = Game(id = 1, name = "Game", year = 2017, publisher = "2k Games", num_players = 4, avg_score = 0, systems = "XONE", theme = "N/A")
        session.add(game)
        session.commit()
        result = session.query(Game).first()
        self.assertEqual(result.name, "Game")
        session.delete(recipe)
	session.commit()

    def test_game_2(self):
	session = self.sess()
        game = Game(id = 1, name = "Game", year = 2017, publisher = "2k Games", num_players = 4, avg_score = 0, systems = "XONE", theme = "N/A")
        session.add(game)
        session.commit()
        result = session.query(Game).first()
        self.assertEqual(result.year, "2017")
        session.delete(game)
	session.commit()

    def test_game_3(self):
	session = self.sess()
        game = Game(id = 1, name = "Game", year = 2017, publisher = "2k Games", num_players = 4, avg_score = 0, systems = "XONE", theme = "N/A")
        session.add(game)
        session.commit()
        result = session.query(Game).first()
        self.assertEqual(result.publisher, "2k Games")
        session.delete(game)
	session.commit()

    def test_genre_1(self):
        session = self.sess()
        genre = Genre(id = 1, name = "Genre", num_games = 100, avg_rating = 3.0, rel_genre = "N/A", popularity = 1)
        session.add(genre)
        session.commit()
        result = session.query(Genre).first()
        self.assertEqual(result.name, "Genre")
        session.delete(genre)
	session.commit()

    def test_genre_2(self):
        session = self.sess()
        genre = Genre(id = 1, name = "Genre", num_games = 100, avg_rating = 3.0, rel_genre = "N/A", popularity = 1)
        session.add(genre)
        session.commit()
        result = session.query(Genre).first()
        self.assertEqual(result.num_games, 100)
        session.delete(genre)
	session.commit()

    def test_genre_3(self):
        session = self.sess()
        genre = Genre(id = 1, name = "Genre", num_games = 100, avg_rating = 3.0, rel_genre = "N/A", popularity = 1)
        session.add(genre)
        session.commit()
        result = session.query(Genre).first()
        self.assertEqual(result.avg_rating, 3.0)
        session.delete(genre)
	session.commit()

    def test_publisher_1(self):
        session = self.sess()
        publisher = Publisher(id = 1, name = "Publisher", num_games = 3, year_founded = 2000, country = "England", num_franchises = 1)
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).first()
        self.assertEqual(result.name, "Publisher")
        session.delete(publisher)
	session.commit()

    def test_publisher_2(self):
        session = self.sess()
        publisher = Publisher(id = 1, name = "Publisher", num_games = 3, year_founded = 2000, country = "England", num_franchises = 1)
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).first()
        self.assertEqual(result.num_games, 3)
        session.delete(publisher)
	session.commit()

    def test_publisher_3(self):
        session = self.sess()
        publisher = Publisher(id = 1, name = "Publisher", num_games = 3, year_founded = 2000, country = "England", num_franchises = 1)
        session.add(publisher)
        session.commit()
        result = session.query(Publisher).first()
        self.assertEqual(result.year_founded, 2000)
        session.delete(publisher)
	session.commit()

        
if __name__ == "__main__":  
main()
