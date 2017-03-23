from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Recipe, Ingredient, Cuisine
from config import test_db

class TestModels (TestCase):

    def test_game_1(self):
        ASSERT(True == True)

    def test_game_2(self):
        ASSERT(True == True)

    def test_game_3(self):
        ASSERT(True == True)

    def test_genre_1(self):
        ASSERT(True == True)

    def test_genre_2(self):
        ASSERT(True == True)

    def test_genre_3(self):
        ASSERT(True == True)

    def test_publisher_1(self):
        ASSERT(True == True)

    def test_publisher_2(self):
        ASSERT(True == True)

    def test_publisher_3(self):
        ASSERT(True == True)
        
if __name__ == "__main__":  
main()
