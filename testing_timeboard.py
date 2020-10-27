import datetime
import timeboard as tb
import timeboard.calendars.US as US
from calendar import monthrange
import pandas as pd

starting_day = datetime.datetime.now().replace(day=1)
ending_day = datetime.datetime.now().replace(day = monthrange(datetime.datetime.now().year, datetime.datetime.now().month)[1])
starting_month = datetime.datetime.now().strftime("%b")
starting_year = datetime.datetime.now().year
tb_start = str(starting_day.day) + ' ' + str(starting_month) + ' ' + str(starting_year)
tb_end = str(ending_day.day) + ' ' + str(starting_month) + ' ' + str(starting_year)
print(tb_start)
print(tb_end)

clnd = tb.Timeboard(base_unit_freq='8H', start=tb_start, end=tb_end,layout=[1,1,1,1,1,0,0])
df = clnd.to_dataframe()
print(clnd)
df.to_excel("testing.xlsx")
