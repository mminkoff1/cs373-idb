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
	__tablename__ = 'games'

	def __init__(self, name, id):
		self.name = name
		self.id = id

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __repr__(self):
		return  self.name 


engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")
engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

resp = requests.get("https://igdbcom-internet-game-database-v1.p.mashape.com/games/?fields=name&limit=10",
                     headers={
					    "X-Mashape-Key": "5nQ6IafYbXmshIQIVdcMhGPqQVhop1NgpLQjsnMyA5A6vqsRXQ"
					 })
data = json.loads(resp.text)

for x in data:
	print x['id']
        print x['name']
        game = Game(x['name'], x['id'])
	session.add(game)
try:
	session.commit()
	print "1"
except:
	session.rollback()
	print "test"
        
"""
game = Game("Minecraft", 2)

try:
	session.add(game)
	session.commit()
	print "1"
except:
	session.rollback()
	print "test"

result = session.query(Game).filter_by(name='Portal').first()

print result
"""
