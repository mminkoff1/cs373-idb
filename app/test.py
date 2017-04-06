
import sys
sys.path.insert(0, './app/')

from flask import Flask
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Game

#connect to database
engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")

Session = sessionmaker(bind = engine)
session = Session()

#get all the data from Game
try:
	data = session.query(Game).all()
except:
	data = "Failed :("

for x in data:
	#encode to UTF-8 in case of any non-ASCII characters
	s = unicode(x).encode('utf8')
	print s
        