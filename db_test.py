import requests
import json 

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask, render_template, make_response, url_for, send_file, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func


Base = declarative_base()

class Game(Base):
	__tablename__ = 'game'

	def __init__(self, name):
		self.name = name

	id = Column(Integer, primary_key=True)
	name = Column(String)


engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")
engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

resp = requests.get("https://igdbcom-internet-game-database-v1.p.mashape.com/games/?fields=name&limit=10",
                     headers={
					    "X-Mashape-Key": "5nQ6IafYbXmshIQIVdcMhGPqQVhop1NgpLQjsnMyA5A6vqsRXQ"
					 })
print (resp.status_code)

data = json.loads(resp.text)

for x in data:
	print x

game = Game("Portal")

try:
	session.add(game)
	print "1"
	session.commit()
except:
	print "test"
	session.rollback()

