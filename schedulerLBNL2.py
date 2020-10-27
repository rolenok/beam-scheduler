import time
import datetime
from app import db
from app.models import Request
import timeboard as tb
import timeboard.calendars.US as US
import pandas as pd
from sqlalchemy import select

# These are sample requests that are made to test out our algorithm
r = Request(id='1',hours=32, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,2,16,0,0))
r1 = Request(id='2',hours=64, scheduled_start=datetime.datetime(2020,10,2,16,0,0),scheduled_end=datetime.datetime(2020,10,4,0,0,0))
r2 = Request(id='3',hours=8, scheduled_start=datetime.datetime(2020,10,3,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r3 = Request(id='4',hours=16, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r4 = Request(id='5',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))#,is_maintenance=True)
r5 = Request(id='6',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r6 = Request(id='7',hours=32, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r7 = Request(id='8',hours=128, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r8 = Request(id='9',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))#,is_maintenace=True)
r9 = Request(id='10',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r12 = Request(id='13',hours=32, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r10 = Request(id='11',hours=16, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r11 = Request(id='12',hours=16, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r13 = Request(id='14',hours=16, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r14 = Request(id='15',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r15 = Request(id='16',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
r16 = Request(id='17',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0))
#Adding the requests into a list so we can commit them to our database model
reqlist=[r,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]
# Printing requests to see if our list of objects worked
# for req in reqlist:
# 	print(req.id, req.hours, req.scheduled_start, req.scheduled_end)

#Adding the rquests into our database model
# for req in reqlist:
# 	db.session.add(req)
# db.session.commit()

# stmt = select('*').select_from(Request)
# result = db.session.execute(stmt).fetchall()
# print(result)
# #req = db.session.query.filter(id='13').first()
# print(r13.id)


def sort_requests_by_duration(reqlist):
	reqlist.sort(key=lambda x: x.hours, reverse=True)

'''
def removeMaintenance(reqlist):
	max_hours= 240
	sortRequestsByDuration(reqlist)
	maintenance = []
		for req in reqlist:
			if (req.is_approved==True):
				schedule.append(req)
				max_hours= max_hours- req.hours
				maintenance.append(req)
				reqlist.remove(req)
	return maintenance
'''

#TODO - Scheduler
#Iterate through list to check if ready, and michaels priority
#if ready and priority is true: schedule to the date the want
#if start date timeslots are all taken, go to next date and try to place the requests
#if date is availaible - schedule
#break down the larger requests in 8s and fill out schedule

def create_schedule(reqlist):
	sort_requests_by_duration(reqlist)
	schedule = []
	maintenance = []
	clnd = US.Weekly8x5() # Creating a calendar so we can see how many work days there are
	currentTime = datetime.datetime.now()
	month = currentTime.strftime("%B")
	year = currentTime.year
	timeboardArg = str(month) + ' ' + str(year)
	timeframe = clnd(timeboardArg, period='M') # makes the timeframe the current month (everything before is just for making a dynamic scheduler)
	max_hours = timeframe.count()*24 # Count of total work days * 24
	# print('Max hours is ' + str(max_hours))
	#max_hours = 240

	for req in reqlist:
		if (req.is_approved==True):
			schedule.append(req)
			max_hours = max_hours- req.hours
			maintenance.append(req)
			reqlist.remove(req)

	for req in reqlist:
		if max_hours>= req.hours:
			schedule.append(req)
			max_hours= max_hours- req.hours

	# print("Schedule: ")
	# for sched in schedule:
	# 	print(sched.hours)
	#
	# print("Maintenance: ")
	# for maint in maintenance:
	# 	print(maint.hours)






#TODO:
#Get all the requests sorted either by a database or by a sorting algorithm (sorted) in python
# sameStart = list()
# for req in reqlist:
# #If start date is the same, check hours
# 	if req.scheduled_start ==

#Assuming all requests are sorted by date we want to then check hours and determine which task takes longest

#Then add this task to the 'Schedule' and find the next longest task and add it on...


create_schedule(reqlist)