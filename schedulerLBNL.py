from flask import Flask, render_template
#from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

import time
import sys

app = Flask(__name__)
cors = CORS(app)
db = SQLAlchemy()
#bcrypt = Bcrypt()

db.init_app(app)
#bcrypt.init_app(app)

class requests(db.Model):
    """Model for the Requests table"""
    __tablename__ = 'requests'

    name = db.Column(db.String(50))
    email = db.Column(db.String(128))
    cell = db.Column(db.String(15))
    company = db.Column(db.String(30))
    integrator = db.Column(db.String(30))
    funding_contact = db.Column(db.String(50))
    address = db.Column(db.String(128))
    city = db.Column(db.String(50))
    state = db.Column(db.String(30))
    zipcode = db.Column(db.Integer())
    approved_integrator = db.Column(db.Boolean())
    approved_facility = db.Column(db.Boolean())
    facility = db.Column(db.String(30))
    ion = db.Column(db.String(30))
    energy = db.Column(db.Float())
    id = db.Column(db.Integer(), primary_key = True)
    funding_cell = db.Column(db.String(15))
    funding_email = db.Column(db.String(128))
    start = db.Column(db.DateTime, nullable=False)
    ions = db.Column(db.ARRAY(db.Integer()))
    comments = db.Column(db.String(200))
    po_number = db.Column(db.Integer())
    username = db.Column(db.String(200))
    beam_time = db.Column(db.Integer())
    scheduled_start = db.Column(db.DateTime)
    integrator_comment = db.Column(db.String(200))
    modified = db.Column(db.Boolean())
    date_of_request = db.Column(db.DateTime)
    status = db.Column(db.String(40))
    rejected = db.Column(db.Boolean())
    order = db.Column(db.Integer())
    request_range = db.Column(db.Integer())
    priority = db.Column(db.Boolean())
    ion_hours = db.Column(db.ARRAY(db.Integer()))
    shifts = db.Column(db.ARRAY(db.Integer()))
    hoursOn = db.Column(db.ARRAY(db.Integer()))
    hoursOff = db.Column(db.ARRAY(db.Integer()))
    totalHours = db.Column(db.ARRAY(db.Integer()))
    personnel = db.Column(db.String(200))
    title = db.Column(db.String(200))

    def create_request(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Beam(id=%s, name=%s, facility=%s)>" % (self.id, self.name, self.facility)


class scheduleLBNL(db.Model):
    __tablename__ = 'scheduleLBNL'

    username = db.Column(db.String(200))
    email = db.Column(db.String(128))
    cell = db.Column(db.String(15))
    scheduled_start = db.Column(db.DateTime)
    hoursOn = db.Column(db.Integer())
    scheduled_end = db.Column(db.DateTime)
    id = db.Column(db.Integer(), primary_key = True)
    energy = db.Column(db.String(15))

    def create_request(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Times(id=%s, start=%s, end=%s)>" % (self.id, self.scheduled_start, self.scheduled_end)


"""TODO: add approved request to database"""

def pushRequest():
	return "Operation Successful. TODO: add approved request to database"

"""TODO: Radix Sort"""
def sortRequests():
	return "TODO: Radix Sort"


def findPerfectSixteens():
	return "TODO: Find Perfect Sixteens"

def findPerfectEights():
	return "TODO: Find Perfect Eights"

@app.route('/', methods=['GET'])

def home():
    return render_template('home.html')

def scheduleLBNL():
    return pushRequest()

if __name__ == '__main__':
	app.run(debug=False)
