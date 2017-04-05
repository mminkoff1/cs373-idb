import requests
import json 

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask, render_template, make_response, url_for, send_file, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
import pybomb

'''
my_key = "3749c81f1b1f295e4fd3bc35baad999a391ac684";
games_client = pybomb.GamesClient(my_key)
return_fields = ('id', 'name', 'expected_release_year', 'publishers', 'themes', 'original_game_rating')
limit = 10
offset = 5
sort_by = 'id'
filter_by = {'game': }

data = games_client.search(
	filter_by = filter_by,
	return_fields=return_fields,
	sort_by = sort_by,
	desc=True,
	limit=limit,
	offset=offset
)

'''
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

headers = {
	'User-agent': 'gamelookup',
}

for i in range(0, 10):

	url_craft = 'https://www.giantbomb.com/api/games/?api_key=3749c81f1b1f295e4fd3bc35baad999a391ac684&format=json&offset=' + str(i * 100);
	r = requests.get(url_craft, headers=headers)


	json_data = r.json()

	for x in json_data['results']:
		print x['id']
		print x['name']
		print x['original_release_date']
		#print x['publishers']
		#print x['original_game_rating']
		#print x['themes']
		#game = Game(x['name'], x['id'], x['year'], x['publisher'], 
		#            x['avg_score'], x['theme'])
		
		#session.add(game)

"""
try:
	session.commit()
	print "1"
except:
	session.rollback()
	print "test"
	"""
