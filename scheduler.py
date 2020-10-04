from flask import Flask, jsonify, request, redirect, url_for, jsonify
#from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask import render_template
from flask import request

from sqlalchemy import create_engine
from Models.models import tamuRequest, nsrlRequest, lbnlRequest, berkleyRequest, db
import time
import sys

appM = Flask(__name__)

"""TESTING"""
appM.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
appM.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requestsv3.db'
db.init_app(appM)

with appM.app_context():
    db.create_all()

"""TODO: Radix Sort"""
def sortRequests():
	return "TODO: Radix Sort"

def findPerfectSixteens():
	return "TODO: Find Perfect Sixteens"

def findPerfectEights():
	return "TODO: Find Perfect Eights"

"""WORK IN PROGRESS: This is the function to render home.html which will allow us
                     to submit requests to the database """
@appM.route('/requestFormPage',methods=['GET','POST'])
def requestFormPage():
    pushRequest()
    return render_template('home.html')

"""WORK IN PROGRESS: This is the function to accept form input from home.html
                     and push the request to the database. """
@appM.route('/pushRequest', methods=['GET','POST'])
def pushRequest():
    try:
        fullName = request.form['name']
        email = request.form['email']
        cell = request.form['cell']
        scheduled_start = request.form['start_date']
        scheduled_end = request.form['end_date']
        hours_req = request.form['hours_req']
        facility = request.form['facility']
        facility = facility.lower()

        """Date formating for the scheduler"""
        scheduled_start = scheduled_start.replace("/"," ").replace("-"," ")
        scheduled_end = scheduled_end.replace("/"," ").replace("-"," ")

        scheduled_start = datetime.strptime(scheduled_start,"%m %d %Y")
        scheduled_end = datetime.strptime(scheduled_end,"%m %d %Y")

        if(facility=="tamu"):
            gen_Request = tamuRequest(name=fullName,email=email,
                                      cell=cell,scheduled_start=scheduled_start,
                                      scheduled_end=scheduled_end,hours_req=hours_req,
                                      facility=facility)
            gen_Request.create_request()
        elif(facility=="nsrl"):
            gen_Request = nsrlRequest(name=fullName,email=email,
                                      cell=cell,scheduled_start=scheduled_start,
                                      scheduled_end=scheduled_end,hours_req=hours_req,
                                      facility=facility)
            gen_Request.create_request()
        elif(facility=="lbnl"):
            gen_Request = lbnlRequest(name=fullName,email=email,
                                      cell=cell,scheduled_start=scheduled_start,
                                      scheduled_end=scheduled_end,hours_req=hours_req,
                                      facility=facility)
            gen_Request.create_request()
        elif(facility=="berkley"):
            gen_Request = berkleyRequest(name=fullName,email=email,
                                         cell=cell,scheduled_start=scheduled_start,
                                         scheduled_end=scheduled_end,hours_req=hours_req,
                                         facility=facility)
            gen_Request.create_request()
        else:
            return "ERROR HERE"


    except Exception as e:
        return(str("ERROR From TRY"))

    return render_template('dbOutput.html',name=gen_Request.name,email=gen_Request.email,
                                           cell = gen_Request.cell, start_date = gen_Request.scheduled_start,
                                           end_date= gen_Request.scheduled_end,
                                           data_info = gen_Request.__repr__(),
                                           hours_req= gen_Request.hours_req,
                                           facility= gen_Request.facility,entry=gen_Request)


"""WORK IN PROGRESS: This function will display all database entries in
                     order by scheduled start date as of now. This will be where
                     the sort function is called as well to continously update database"""
@appM.route('/checkTamu', methods=['GET','POST'])
def checkTamu():
    requests = tamuRequest.query.order_by(tamuRequest.scheduled_start)
    return render_template('tamuSchedule.html', requests=requests)

@appM.route('/checkLBNL', methods=['GET','POST'])
def checkLBNL():
    requests = lbnlRequest.query.order_by(lbnlRequest.scheduled_start)
    return render_template('lbnlSchedule.html', requests=requests)

@appM.route('/checkNSRL', methods=['GET','POST'])
def checkNSRL():
    requests = nsrlRequest.query.order_by(nsrlRequest.scheduled_start)
    return render_template('nsrlSchedule.html', requests=requests)

@appM.route('/checkBerkley', methods=['GET','POST'])
def checkBerkley():
    requests = berkleyRequest.query.order_by(berkleyRequest.scheduled_start)
    return render_template('berkleySchedule.html', requests=requests)

if __name__ == '__main__':
    appM.run(debug=False)
