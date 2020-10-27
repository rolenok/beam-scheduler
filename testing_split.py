import time
import datetime
from app import db
from app.models import Request
import timeboard as tb
import timeboard.calendars.US as US
import pandas as pd
import copy
from calendar import monthrange
import xlrd


starting_day = datetime.datetime.now().replace(day=1)
ending_day = datetime.datetime.now().replace(day = monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1])
starting_month = datetime.datetime.now().strftime("%b")
starting_year = datetime.datetime.now().year
tb_start = str(starting_day.day) + ' ' + str(starting_month) + ' ' + str(starting_year)
tb_end = str(ending_day.day) + ' ' + str(starting_month) + ' ' + str(starting_year)
# print(tb_start)
# print(tb_end)

clnd = tb.Timeboard(base_unit_freq='8H', start=tb_start, end=tb_end,layout=[0,0,0,0,0,0,0])
#df = clnd.to_dataframe()
#print(clnd)
df1 = pd.read_excel(r'/home/ssv594/beamscheduler/beam-scheduler/test_data.xlsx')
# print(df1)
req_list = list()
for index, row in df1.iterrows():
	new_row = Request(id=row['id'], hours=row['hours'],scheduled_start=row['scheduled_start'],scheduled_end=row['scheduled_end'],is_approved=row['is_approved'],proj_id=row['proj_id'], is_priority=row['is_priority'])
	req_list.append(new_row)
# req_list = Request(df1.values.tolist())

#
# r2 = Request(id='3',hours=8, scheduled_start=datetime.datetime(2020,10,3,0,0,0), scheduled_end=datetime.datetime(2020,10,3,0,0,0), is_approved=False, proj_id=1)
# r3 = Request(id='4',hours=16, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,2,0,0,0), is_approved=False, proj_id=2)
# r4 = Request(id='5',hours=8, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,1,0,0,0), is_approved=False, proj_id=3)#,is_maintenance=True)
# r5 = Request(id='6',hours=8, scheduled_start=datetime.datetime(2020,10,3,0,0,0), scheduled_end=datetime.datetime(2020,10,3,0,0,0), is_approved=True,  proj_id=4)
# r7 = Request(id='8',hours=129, scheduled_start=datetime.datetime(2020,10,1,0,0,0), scheduled_end=datetime.datetime(2020,10,10,0,0,0), is_approved=True,  proj_id=5, is_priority=True)
#
# req_list = [r2,r3,r4,r5,r7]
id_num = 0

def split_request(Request):
	hours = Request.hours #get total hours of the request
	count = 0

	if(hours%8 == 0): # if request hours is divisible by 8, we want to add a counter to loop and make request
		count = hours//8

	else: # if request hours isnt divisble by 8, get the count and the remaining hours
		count = hours//8 # integer division for Count
		#count = count + 1 # extra count iteration to make a request with the remaining hours
		remaining_hours = hours%8

	sub_requests_list1 = [Request for i in range(count)] #duplicates the correct amount of Requests in a list
	sub_requests_list2 = list() # Blank list to store the modified requests


	for sub in sub_requests_list1:

		# sub.workday = sub.scheduled_start + datetime.timedelta(hours=8*num_iters)
		sub.id = 0
		sub_requests_list2.append(copy.deepcopy(sub)) # Makes a unique copy (instance) of each request
		sub.hours = sub.hours - 8 # decrementing the hours left
		count = count - 1
		# id_num = id_num + 1
		#print(str(sub.id) + ' and ' + str(sub.hours) + '\n')

	# print('SUB LIST 2:')
	# for x in sub_requests_list2:
	# 	print(str(x.id) + ' ' + str(x.hours))
	# #print(sub_requests_list1)

	return sub_requests_list2

def normalize_id(to_be_scheduled): # Function to make sure each request has a unique id
	global id_num
	for req in to_be_scheduled:
		req.id = id_num
		id_num = id_num + 1


to_be_scheduled = list() #Master list of every request even the split ones

for req in req_list:
	if (req.hours > 8): #Splitting the requests
		to_be_scheduled.extend(split_request(req)) #Adding them to the master list

	else:
		req.workday = req.scheduled_start
		to_be_scheduled.append(req) # requests didnt need to be split, add it to the master list


def assign_workday(to_be_scheduled):
	mornings_used = 0
	evening_used = 0
	mid_used = 0
	slots_used = 0
	for sub in to_be_scheduled:
		if to_be_scheduled.index(sub)-1 < 0:
			pass
		if sub.proj_id != to_be_scheduled[to_be_scheduled.index(sub)-1].proj_id:
			mornings_used = 0
			evening_used = 0
			mid_used = 0
			slots_used = 0

		count = sum(req.proj_id == sub.proj_id for req in to_be_scheduled)

		total_days = (sub.scheduled_end - sub.scheduled_start).days

		if slots_used < count and mornings_used < total_days:
			sub.workday = sub.scheduled_start + datetime.timedelta(hours=24*mornings_used)
			mornings_used = mornings_used + 1
			slots_used = slots_used + 1
			# print('used {} mornings of {} available'.format(mornings_used, total_days))

		elif slots_used < count and evening_used < total_days and mornings_used >= total_days:
			sub.workday = sub.scheduled_start + datetime.timedelta(hours=16) + datetime.timedelta(hours=24*evening_used)
			evening_used = evening_used + 1
			slots_used = slots_used + 1
			# print('used {} evenings of {} available'.format(evening_used, total_days))

		elif slots_used < count and mid_used < total_days and evening_used >= total_days:
			sub.workday = sub.scheduled_start + datetime.timedelta(hours=8) + datetime.timedelta(hours=24*mid_used)
			mid_used = mid_used + 1
			slots_used = slots_used + 1
			# print('used {} mids of {} available'.format(mid_used, total_days))
		else:
			pass



def get_priority_reqs(to_be_scheduled):
	priority_reqs = list()
	for req in to_be_scheduled:
		if req.is_priority == True:
			priority_reqs.append(req)
	return priority_reqs

def schedule_the_requests(to_be_scheduled):
	# for req in to_be_scheduled:
	# 	#if 4 items with same day, check priority of 4 items
	# 	#If priority = true youre placed in that day if 3 items have not been placed yet
	# 	#If priority but 3 items have been placed,
	priorit_reqs = get_priority_reqs(to_be_scheduled)



# for req in to_be_scheduled:
# 	print(str(req.workday) + ' and ' + str(req.id) + ' aand ' + str(req.proj_id) + '\n')

normalize_id(to_be_scheduled) #Call normalize_id to make the requests ids unique
assign_workday(to_be_scheduled)
for x in to_be_scheduled:
	print(x.workday)


schedule_the_requests(to_be_scheduled)

df = clnd.to_dataframe() # Make timeboard a dataframe so we can send it to excel sheet
#df.to_excel("testing.xlsx")

# print('This is the start')
# print(to_be_scheduled)








# split_request(r7)
