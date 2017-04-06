
import sys, traceback
sys.path.insert(0, './app/')

from flask import Flask, render_template, jsonify, request
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import Game, Publisher, Character
       
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'
app.config.from_object(__name__) # load config from this file , flaskr.py


#connect to database
engine = create_engine("postgresql://" + "postgres" + ":" + "seanpickupyourphone" + "@" + "35.184.159.10" + "/" + "gamelookup")

Session = sessionmaker(bind = engine)
session = Session()


@app.route('/')
def splash():
	return render_template("splash.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/games')
def games():
	return render_template("games.html",
		games = session.query(Game).all())

@app.route('/genre')
def genre():
	return render_template("genre.html")


@app.route('/api/games')
def gamedata():
	try:
		data = session.query(Game).all()
	except:
		data = "Failed :("
		#print (data)
	return jsonify(games_list=[i.serialize for i in data])


@app.route('/api/publishers')
def gamedata():
	try:
		data = session.query(Publisher).all()
	except:
		data = "Failed :("
		#print (data)
	return jsonify(publishers_list=[i.serialize for i in data])


@app.route('/api/characters')
def gamedata():
	try:
		data = session.query(Character).all()
	except:
		data = "Failed :("
		#print (data)
	return jsonify(characters_list=[i.serialize for i in data])


# SHUTDOWN CODE FOR DEBUGGING -REMOVE BEFORE DEPLOYING #
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

# SHUTDOWN CODE FOR DEBUGGING -REMOVE BEFORE DEPLOYING #
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'



if __name__ == "__main__":
	app.run()
