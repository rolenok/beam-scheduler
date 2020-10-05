from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(UserMixin, db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	facility = db.Column(db.String(64), index=True, unique= False)
	is_integrator = db.Column(db.Boolean, default = False)
	is_facility_admin = db.Column(db.Boolean, default=False)
	company = db.Column(db.String(64), index=True, unique=False)
	fname = db.Column(db.String(28), index=True, unique=False)
	lname = db.Column(db.String(28), index=True, unique=False)
	requests = db.relationship('Request', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


class Request(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	facility = db.Column(db.String(64), index = True, unique = False)
	#is_integrator_request = db.Column(db.Boolean, db.ForeignKey('user.is_integrator'))
	#company = db.Column(db.String(64), db.ForeignKey('user.company'), index = True, unique = False)
	user_id = db.Column(db.String(64), db.ForeignKey('user.id'), index= True, unique = True)
	is_approved= db.Column(db.Boolean, default = False)
	status = db.Column(db.String(16), index=True, unique= False)
	beam = db.Column(db.String(16), index=True, unique = False)
	ion = db.Column(db.Integer, index = True, unique = False)
	energy = db.Column(db.Integer, index = True)
	fluence = db.Column(db.Integer, index = True)
	flux = db.Column(db.Integer, index = True)
	LET = db.Column(db.Integer, index = True)
	hours = db.Column(db.Integer, index = True)
	beam_size = db.Column(db.Integer, index = True)
	#range = db.Column()
	scheduled_start = db.Column(db.DateTime)
	scheduled_end = db.Column(db.DateTime)

	def __repr__(self):
		return '<Request {}>'.format(self.id)    

'''
class NSRL(db.Model):
#TODO add timeboard as base_schedule

class LBNL(db.Model):
#TODO add timeboard as base_schedule

class TAMU(db.Model):
#TODO add timeboard as base_schedule

class Berkley(db.Model):
#TODO add timeboard as base_schedule

class scheduleLBNL(db.Model):
class scheduleNSRL(db.Model):
class scheduleTAMU(db.Model):
class scheduleBerkley(db.Model):

'''

