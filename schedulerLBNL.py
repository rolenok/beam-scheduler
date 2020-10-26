import time
from datetime import datetime
from app import db
from app.models import Request, User


r = Request(scheduled_start=datetime(2020,1,1,0,0,0), scheduled_end=datetime(2020,1,2,0,0,0))
r1 = Request(scheduled_start=datetime(2020,1,2,8,0,0), scheduled_end=datetime(2020,1,4,16,0,0))
r2 = Request(scheduled_start=datetime(2020,1,5,16,0,0), scheduled_end=datetime(2020,1,7,8,0,0))
r3 = Request(scheduled_start=datetime(2020,1,8,8,0,0), scheduled_end=datetime(2020,1,10,8,0,0))
r4 = Request(scheduled_start=datetime(2020,1,16,0,0,0), scheduled_end=datetime(2020,1,20,16,0,0))
r5= Request(scheduled_start=datetime(2020,1,21,0,0,0), scheduled_end=datetime(2020,1,23,16,0,0))
r6 = Request(scheduled_start=datetime(2020,1,25,0,0,0), scheduled_end=datetime(2020,1,27,16,0,0))
r7 = Request(scheduled_start=datetime(2020,1,23,0,0,0), scheduled_end=datetime(2020,1,24,0,0,0), is_maintenance=True)

reqlist=[r1,r2,r3,r4,r5,r6,r7]
# Printing requests to see if our list of objects worked
# for req in reqlist:
# 	print(req.id, req.hours, req.scheduled_start, req.scheduled_end)

#Adding the rquests into our database model
#for req in reqlist:
#	db.session.add(req)
#db.session.commit()

def sort_requests_by_duration(reqlist, max_hours):
	reqlist.sort(key=lambda x: x.hours, reverse=True)

def sort_requests_by_priority(reqlist):
	reqlist.sort(key=lambda x: x.is_maintenance, reverse=True)

def create_request_duration():
	#Getting time between two dates
	try: 
		query = db.session.query(Request)
		for req in query:
			time_between = req.scheduled_end - req.scheduled_start
			print(time_between)
			req.hours = time_between
			db.session.commit()

	except Exception as e:
		print(e)
	#print(time_between)

def split_requests(reqlist):
	# max range is the preferred amount of time between each shift
	# max shifts is the preferred amount of shifts into which we will split up the time
	try:
		requests_to_split = []
		for req in reqlist:
			if req.is_splittable == True:
				requests_to_split.append(req)
				req.split == True
				req.is_splittable == False

	except Exception as e:
		print(e)

	return requests_to_split

def process_split_requests(requests_to_split):
	try :
		schedule = []
		for req in requests_to_split:
			if (req.split == True):
				schedule.append(req)
				req.hours = req.hours - 8;
				#if range == 5:	
					#then the max value between shifts can be 5 days 

def modulo_hours(reqlist):
	for req in reqlist:
		if ((req.hours % 8) != 0):
			h = req.hours % 8
			req.hours = req.hours + h;

def assign_priority(reqlist):

	try: 
		for req in reqlist:
			req.author.priority=req.priority
			if req.stale == True:
				req.priority = 3; # high
			elif req.is_maintenance == True:
				req.priority = 4; # ultimate

	except Exception as e:
		print(e)


'''
def is_stale(reqlist):
	try:

		#for req in reqlist: 
		#	if req.

	except Exception as e:
		print(e)
'''
#TODO:Construction Heuristic
	#find feasible solution(s)


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

#p1 == hours
#p2 == fluence
def sort_by_priority(reqlist, p1, p2, p3): 
	schedule = []
	p_max = 0;
	tmp_reqlist = reqlist

	for req in tmp_reqlist:
		if (req.p1 >= p_max):
			req.p1 = p_max
			schedule.append(req)
			tmp_reqlist.remove(req)

	tmp_reqlist = reqlist
	p_max = 0

	while (!reqlist.is_empty()):
		for req in tmp_reqlist: 
			if (req.p2 >= p_max):
				req.p2 = p_max
				tmp = req
				tmp.range = tmp.scheduled_start - tmp.scheduled_end
				for req in reqlist:

					if req.range != tmp.range
						schedule.append(tmp)  
	
	while (!reqlist.is_empty()):
	tmp_reqlist = reqlist
	p_max = 0
	for req in tmp_reqlist:
		if req.p3 >= p_max:
			req.p3 = p_max
			tmp = req
			tmp.range = tmp.scheduled_start - tmp_scheduled_end
			for req in reqlist:
				if req.range != tmp.range


def create_schedule(reqlist, max_hours):
	try: 
		sort_requests_by_duration(reqlist, max_hours)
		schedule = []
		maintenance = []
		for req in reqlist:
			if (req.is_approved==True):
				schedule.append(req)
				max_hours= max_hours- req.hours
				maintenance.append(req)
				reqlist.remove(req)
		
		for req in reqlist:
			if max_hours>= req.hours:
				schedule.append(req)
				max_hours= max_hours- req.hours

		print("Schedule: ")
		for sched in schedule:
			print(sched.hours)

		print("Maintenance: ")
		for maint in maintenance:
			print(maint.hours)

		db.session.commit()
	except Exception as e:
		print(e)




#TODO:
#Get all the requests sorted either by a database or by a sorting algorithm (sorted) in python
# sameStart = list()
# for req in reqlist:
# #If start date is the same, check hours
# 	if req.scheduled_start ==

#Assuming all requests are sorted by date we want to then check hours and determine which task takes longest

#Then add this task to the 'Schedule' and find the next longest task and add it on...

#max_hours = 240
#create_schedule(reqlist,max_hours)
