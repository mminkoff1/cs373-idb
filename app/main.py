from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test@localhost/swe'
'''
db = SQLAlchemy(app)

class Students(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	grader_id = db.Column(db.Integer, db.ForeignKey('graders.id'))
	grader = db.relationship('Graders', back_populates="students")

class Graders(db.Model):
	__tablename__ = 'graders'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String)
	students = db.relationship('Students', back_populates="grader")
'''

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

@app.route('/publisher')
def publisher():
	return render_template("publisher.html")

if __name__ == "__main__":
	app.run()
