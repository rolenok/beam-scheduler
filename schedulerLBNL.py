from flask import Flask, jsonify, request, redirect, url_for, jsonify
#from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask import render_template
from flask import request

from sqlalchemy import create_engine

import time
import sys

app = Flask(__name__)

"""TESTING"""
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests2.db'

cors = CORS(app)
db = SQLAlchemy(app)
#bcrypt = Bcrypt()
#bcrypt.init_app(app)

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

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),nullable=False)
    cell = db.Column(db.String(255),nullable=False)
    scheduled_start = db.Column(db.String(255),nullable=False)
    scheduled_end = db.Column(db.String(255),nullable=False)
    hours_req = db.Column(db.Integer, nullable=False)

    createdDate = db.Column(db.DateTime,default=datetime.utcnow)
    """createdFormatDate = time.strftime("%m%d%y",createdDate)"""

    def create_request(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return "<Times(id=%s, start=%s, end=%s createdOn=%s)>" % (self.id, self.scheduled_start,
                                                                  self.scheduled_end, self.createdDate)



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
        hours_req = request.form['hours_req']

        """Date formating for the scheduler"""
        scheduled_start = scheduled_start.replace("/"," ").replace("-"," ")
        scheduled_end = scheduled_end.replace("/"," ").replace("-"," ")

        scheduled_start = datetime.strptime(scheduled_start,"%m %d %Y")
        scheduled_end = datetime.strptime(scheduled_end,"%m %d %Y")

        gen_Request = testRequest()
        gen_Request.name = fullName
        gen_Request.email = email
        gen_Request.cell = cell
        gen_Request.scheduled_start = scheduled_start
        gen_Request.scheduled_end = scheduled_end
        gen_Request.hours_req = hours_req
        gen_Request.create_request()

    except Exception as e:
        return(str(e))

    return render_template('dbOutput.html',name=gen_Request.name,email=gen_Request.email,
                                           cell = gen_Request.cell, start_date = gen_Request.scheduled_start,
                                           end_date= gen_Request.scheduled_end,
                                           data_info = gen_Request.__repr__(),
                                           hours_req= gen_Request.hours_req ,entry=gen_Request)


"""WORK IN PROGRESS: This function will display all database entries in
                     order by scheduled start date as of now. This will be where
                     the sort function is called as well to continously update database"""
@app.route('/checkSchedule', methods=['GET','POST'])
def checkSchedule():
    requests = testRequest.query.order_by(testRequest.scheduled_start)
    return render_template('checkSchedule.html', requests=requests)



if __name__ == '__main__':
    app.run(debug=False)
