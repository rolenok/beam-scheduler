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

db = SQLAlchemy()

"""Nsrl, tamu, Lbnl, and Berkeley database models"""

class tamuRequest(db.Model):
    __tablename__ = 'tamuRequest'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    facility = db.Column(db.String(255),nullable=False)
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

class lbnlRequest(db.Model):
    __tablename__ = 'lbnlRequest'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    facility = db.Column(db.String(255),nullable=False)
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

class nsrlRequest(db.Model):
    __tablename__ = 'nsrlRequest'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    facility = db.Column(db.String(255),nullable=False)
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

class berkleyRequest(db.Model):
    __tablename__ = 'berkleyRequest'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    facility = db.Column(db.String(255),nullable=False)
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
