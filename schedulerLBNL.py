from flask import Flask
#from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask import render_template
from flask import request

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

class testRequest(db.Model):
    __tablename__ = 'testRequest'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),nullable=False)
    cell = db.Column(db.String(255),nullable=False)
    scheduled_start = db.Column(db.String(255),nullable=False)
    scheduled_end = db.Column(db.String(255),nullable=False)
    createdOn = db.Column(db.DateTime(),default=datetime.utcnow)

    """dataInfo = "<Times(id=%s, start=%s, end=%s createdOn=%s)>" % (this.id,this.scheduled_start,
                                                                  this.scheduled_end,this.createdOn)"""
    def create_request(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Times(id=%s, start=%s, end=%s createdOn=%s)>" % (self.id, self.scheduled_start,
                                                                  self.scheduled_end, self.createdOn)

"""TODO: Radix Sort"""
def sortRequests():
	return "TODO: Radix Sort"

def findPerfectSixteens():
	return "TODO: Find Perfect Sixteens"

def findPerfectEights():
	return "TODO: Find Perfect Eights"

"""WORK IN PROGRESS: This is the function to render home.html which will allow us
                     to submit requests to the database """
@app.route('/requestFormPage',methods=['GET','POST'])
def requestFormPage():
    pushRequest()
    return render_template('home.html')

"""WORK IN PROGRESS: This is the function to accept form input from home.html
                     and push the request to the database. """
@app.route('/pushRequest', methods=['GET','POST'])
def pushRequest():
    try:
        fullName = request.form['name']
        email = request.form['email']
        cell = request.form['cell']
        scheduled_start = request.form['start_date']
        scheduled_end = request.form['end_date']

        gen_Request = testRequest()
        gen_Request.name = fullName
        gen_Request.email = email
        gen_Request.cell = cell
        gen_Request.scheduled_start = scheduled_start
        gen_Request.scheduled_end = scheduled_end


    except Exception as e:
        return(str(e))

    return render_template('dbOutput.html',name=gen_Request.name,email=gen_Request.email,
                                           cell = gen_Request.cell, start_date = gen_Request.scheduled_start,
                                           end_date= gen_Request.scheduled_end,
                                           data_info = gen_Request.__repr__())

@app.route('/test1', methods=['GET'])
def scheduleLBNL():
    return pushRequest()


if __name__ == '__main__':
    app.run(debug=False)
