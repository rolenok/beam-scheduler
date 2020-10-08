import time
import datetime
from app import db
from app.models import Request

print('hello world')

r = Request(id='1',hours='32', scheduled_start="2020-10-2", scheduled_end="2020-10-4")
r1 = Request(id='2',hours='64', scheduled_start="2020-10-5", scheduled_end='2020-10-8')
r2 = Request(id='3',hours='8', scheduled_start="2020-9-10", scheduled_end='2020-10-9')
r3 = Request(id='4',hours='16', scheduled_start="2020-10-10", scheduled_end='2020-10-10')
r4 = Request(id='5',hours='8', scheduled_start="2020-10-11", scheduled_end='2020-10-11')
r5 = Request(id='6',hours='4', scheduled_start="2020-10-11", scheduled_end='2020-10-11')
r6 = Request(id='7',hours='32', scheduled_start="2020-10-12", scheduled_end='2020-10-13')
r7 = Request(id='8',hours='128', scheduled_start="2020-10-14", scheduled_end='2020-10-18')
r8 = Request(id='9',hours='4', scheduled_start="2020-10-19", scheduled_end='2020-10-19')
r9 = Request(id='10',hours='8', scheduled_start="2020-10-19", scheduled_end='2020-10-19')
r12 = Request(id='13',hours='32', scheduled_start="2020-10-19", scheduled_end='2020-10-20')
r10 = Request(id='11',hours='16', scheduled_start="2020-10-21", scheduled_end='2020-10-21')
r11 = Request(id='12',hours='16', scheduled_start="2020-10-22", scheduled_end='2020-10-22')
r13 = Request(id='14',hours='16', scheduled_start="2020-10-23", scheduled_end='2020-10-23')
r14 = Request(id='15',hours='8', scheduled_start="2020-10-24", scheduled_end='2020-10-24')
r15 = Request(id='16',hours='8', scheduled_start="2020-10-24", scheduled_end='2020-10-24')
r16 = Request(id='17',hours='4', scheduled_start="2020-10-25", scheduled_end='2020-10-25')

reqlist=[r,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16]
	#print(reqlist)
for req in reqlist:
	print(req.id, req.hours, req.scheduled_start, req.scheduled_end)

	#reqlist=[]
	#reqlist.append(Request(id='1',hours='32', scheduled_start="2020-10-2", scheduled_end="2020-10-4"))

	#print(reqlist)

	#for req in reqlist:
	#	db.session.add(req)

	#b.session.commit()



