import datetime
import timeboard as tb
import timeboard.calendars.US as US

# #Working hours (8-5) in a month
# clnd = US.Weekly8x5()
# currentTime = datetime.datetime.now()
# month = currentTime.strftime("%B")
# year = currentTime.year
# timeboardArg = str(month) + ' ' + str(year)
# timeframe = clnd(timeboardArg, period='M')
# print(timeframe.worktime())
# # print(month.strftime("%b"))
# #print(timeboardArg)

# clnd = US.Weekly8x5()
# currentTime = datetime.datetime.now()
# month = currentTime.strftime("%B")
# year = currentTime.year
# timeboardArg = str(month) + ' ' + str(year)
# timeframe = clnd(timeboardArg, period='M')
# max_hours = timeframe.count()*24
# print(max_hours)

#Getting time between two dates
end_date = datetime.datetime(2020, 10, 19, 0, 0, 0)
start_date = datetime.datetime(2020,10,3,8,0,0)
time_between = end_date - start_date
#print(time_between)
