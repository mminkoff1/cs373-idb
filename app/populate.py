import requests
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Float, Integer, String, Boolean,ForeignKey, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from flask import Flask, render_template, make_response, url_for, send_file, jsonify, request
from sqlalchemy.orm import sessionmaker
import pybomb
from sqlalchemy.sql import table, column, select, update, insert

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

	def __init__(self, ident, name, year, publisher, avg_score, theme):
                self.ident = ident
		self.name = name
		self.year = int(year)
                self.publisher = publisher
                self.avg_score = avg_score
                self.theme = theme

	ident = Column(Integer, primary_key=True)
	name = Column(String)
        year = Column(Integer)
        publisher = Column(String)
        avg_score = Column(String)
        theme = Column(String)

	def __repr__(self):
		return  self.name 


engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")
conn = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

headers = {
	'User-agent': 'gamelookup',
}
publishermap = {}
publishers = []
'''
for i in range(0, 1):

	url_craft = 'https://www.giantbomb.com/api/games/?api_key=3749c81f1b1f295e4fd3bc35baad999a391ac684&format=json&offset=' + str(i * 100);
	r = requests.get(url_craft, headers=headers)


	json_data = r.json()

	for x in json_data['results']:
		print x['id']
		print x['name']
		#print x['publishers']
		#print x['original_game_rating']
		#print x['themes']

                if x['original_release_date'] != None:
                    original_release_date = int(x['original_release_date'][:4])
                else:
                    original_release_date = 0
                print original_release_date
		game = Game(x['id'], x['name'], int(original_release_date), 'N/A', 'N/A', 'N/A')

         	session.add(game)

                url_craft2 = 'https://www.giantbomb.com/api/game/' + str(x['id']) + '/?api_key=3749c81f1b1f295e4fd3bc35baad999a391ac684&format=json'
                r2 = requests.get(url_craft2, headers=headers)

                json_data2 = r2.json()

                idee = x['id']
                
                pubpre = json_data2['results']['publishers']
                ratepre = json_data2['results']['original_game_rating']

                if 'themes' in json_data2['results']:
                    themepre = json_data2['results']['themes']
                else:
                    themepre = None

                if pubpre != None:
                    pub = json_data2['results']['publishers'][0]['name']
                    publishers.append(pub)
                else: 
                    pub = 'N/A'

                if ratepre != None:
                    rate = json_data2['results']['original_game_rating'][0]['name']
                else: 
                    rate = 'N/A'

                if themepre != None:
                    theme = json_data2['results']['themes'][0]['name']
                else: 
                    theme = 'N/A'

                session.query(Game).filter_by(ident=idee).update({Game.publisher: pub})
                session.query(Game).filter_by(ident=idee).update({Game.avg_score: rate})
                session.query(Game).filter_by(ident=idee).update({Game.theme: theme})

                session.commit()


#session.query(Game).filter_by(ident=6).update({Game.publisher: u"EA GAMES"})

session.commit()
'''
publishers = [r.publisher for r in session.query(Game.publisher).distinct()]

ser = open('publisherout.txt', 'r').read()
publishersmap = eval(ser)

for publ in publishers:

    if publ != 'N/A':
        pubid = publishersmap.get(publ)
    else:
        continue

    url_craft4 = 'https://www.giantbomb.com/api/company/' + str(pubid) + '/?api_key=3749c81f1b1f295e4fd3bc35baad999a391ac684&format=json'
    r4 = requests.get(url_craft4, headers=headers)

    json_data4 = r4.json()

    print len(json_data4['results']['published_games'])

'''
for i in range(0, 132):
    url_craft3 = 'https://www.giantbomb.com/api/companies/?api_key=3749c81f1b1f295e4fd3bc35baad999a391ac684&format=json&offset=' + str(i * 100)
    r3 = requests.get(url_craft3, headers=headers)

    json_data3 = r3.json()

    for x in json_data3['results']:
        namee = x['name']
        idd = x['id']

        publishermap[namee] = idd

#newpubmap = json.load(open("publisherout.txt"))

#print newpubmap

print publishermap
'''
#print "1"
