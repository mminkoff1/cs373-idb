
import sys, traceback
sys.path.insert(0, './app/')

from flask import Flask, render_template, jsonify
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Game, Publisher
       
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'
app.config.from_object(__name__) # load config from this file , flaskr.py


#connect to database
engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")

Session = sessionmaker(bind = engine)
session = Session()


# for x in data:
# 	#encode to UTF-8 in case of any non-ASCII characters
# 	s = unicode(x.avg_score).encode('utf8')
# 	print s

@app.route('/')
def splash():
	return render_template("splash.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/games')
def games():
	return render_template("games.html")

@app.route('/genre')
def genre():
	return render_template("genre.html")

@app.route('/gamedata')
def gamedata():
	try:
		data = session.query(Game).all()
	except:
		data = "Failed :("
		#print (data)
	return jsonify(data)





if __name__ == "__main__":
	app.run()
