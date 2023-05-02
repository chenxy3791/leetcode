# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:02:42 2021

@author: chenxy
"""

# 1. What is inside datetime?
import datetime
print(dir(datetime))

# Example 1: Get Current Date and Time
now = datetime.datetime.now()
print(now)

# Commonly used classes in the datetime module are:
# (1). date Class
# (2). time Class
# (3). datetime Class
# (4). timedelta Class
from datetime import date, time ,datetime, timedelta

# 2. date Class
# Example 2: Date object to represent a date
# date() in the above example is a constructor of the date class. 
# The constructor takes three arguments: year, month and day.
d = date(2021,10,26)
print(d)

# Example 3: Get current date
today = date.today()
print(today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Example 4: Get date from a timestamp
print('Example 4:...')
d = date.fromtimestamp(1158676809.864)
print(d)
# What is the start for the timestamp?
d0 = date.fromtimestamp(0)
print(d0)

# Example 4-1: Get the timestamp of a date
tstr = '10/23/2011 20:44:24.990'

dobj = datetime.strptime(tstr, "%m/%d/%Y %H:%M:%S.%f")
print(dobj)
print(datetime.fromtimestamp(dobj.timestamp()))

# 3. time Class

# Example 5: Time object to represent time
# time(hour = 0, minute = 0, second = 0)
print('\nExample 5:...')
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)
print("hour =", d.hour)
print("minute =", d.minute)
print("second =", d.second)
print("microsecond =", d.microsecond)

# 4. datetime.datetime
# The datetime module has a class named datetime that can contain information 
# from both date and time objects.
# Example 6: Python datetime object

print('\nExample 6:...')
#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)
print("year =", b.year)
print("month =", b.month)
print("hour =", b.hour)
print("minute =", b.minute)
print("timestamp =", b.timestamp())

# 5. datetime.timedelta
# A timedelta object represents the difference between two dates or times.

from datetime import datetime, date

print('\nExample 7:...')
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))  
# Notice, both t3 and t6 are of <class 'datetime.timedelta'> type.

# Example 8: Difference between two timedelta objects

print('\nExample 8:...')
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)
print("type of t1 =", type(t1)) 
print("type of t2 =", type(t2))  
print("type of t3 =", type(t3))  

# Example 9: Printing negative timedelta object

from datetime import timedelta
print('\nExample 9:...')
t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2
print("t3 =", t3)
print("t3 =", abs(t3))

# Example 10: Time duration in seconds
# You can get the total number of seconds in a timedelta object using total_seconds() method.
print('\nExample 10:...')
t1 = timedelta(seconds = 33)
t2 = timedelta(seconds = 54)
t3 = t1 - t2
print("total seconds =", t3.total_seconds())
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("total seconds =", t.total_seconds())

# You can also find sum of two dates and times using + operator. 
# Also, you can multiply and divide a timedelta object by integers and floats.
# ??? The following code segment doesn't work.
# print('\nExample 11:...')
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 + t2
# print(t3)


# 6. Python format datetime
# The way date and time is represented may be different in different places, 
# organizations etc. It's more common to use mm/dd/yyyy in the US, 
# whereas dd/mm/yyyy is more common in the UK.

# Python has strftime() and strptime() methods to handle this.

# 6.1 Python strftime() - datetime object to string
# The strftime() method is defined under classes date, datetime and time. 
# The method creates a formatted string from a given date, datetime or time object.
# Format codes in strftime()
# %Y - year [0001,..., 2018, 2019,..., 9999]
# %m - month [01, 02, ..., 11, 12]
# %d - day [01, 02, ..., 30, 31]
# %H - hour [00, 01, ..., 22, 23
# %M - minute [00, 01, ..., 58, 59]
# %S - second [00, 01, ..., 58, 59]
# Example 15: Format date using strftime()

# current date and time
print('\nExample 12:...')
now = datetime.now()

t = now.strftime("%H:%M:%S")
print('type of t is ',type(t))
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

s3 = now.strftime("%d/%m/%y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s3:", s3)

s4 = now.strftime("%y-%m-%d, %H:%M:%S")
# yy-mm-dd H:M:S format
print("s4:", s4)

# 5.2 Python strptime() - string to datetime
# The strptime() method creates a datetime object from a given string (representing date and time).

# Example 13: strptime()
print('\nExample 13:...')
date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# The strptime() method takes two arguments:

# a string representing date and time
# format code equivalent to the first argument
# By the way, %d, %B and %Y format codes are used for day, month(full name) and year respectively.

# 7. Handling timezone in Python
# Suppose, you are working on a project and need to display date and time based on their timezone. 
# Rather than trying to handle timezone yourself, we suggest you to use a third-party pytZ module.

from datetime import datetime, timezone
import pytz

print('\nExample 14...')
print('\ncommon pytz timezone list...')
print(len(pytz.common_timezones))
# print(pytz.common_timezones)
print(len(pytz.all_timezones))
# print(pytz.all_timezones)


print('\nExample 15:...')
local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_SH = pytz.timezone('Asia/Shanghai') 
datetime_SH = datetime.now(tz_SH)
print("SH:", datetime_SH.strftime("%m/%d/%Y, %H:%M:%S"))

timeDifference = (datetime_SH - datetime_NY)
print('Time difference between SH and NY is:',timeDifference) # Doesn't work properly.


# # 1. 
# import time
# timestamp0_str = '30/03/09 16:31:32'
# a = time.strptime(timestamp0_str, '%d/%m/%y %H:%M:%S')
# print(a)

# # The strptime() method creates a datetime object from the given string.
# # Note: You cannot create datetime object from every string. The string needs to be in a certain format.
# from datetime import datetime
# t_string = "21 June, 2018"
# print("date_string =", t_string)
# print("type of date_string =", type(t_string))

# t_dt_object = datetime.strptime(t_string, "%d %B, %Y")

# print("date_object =", t_dt_object)
# print("type of date_object =", type(t_dt_object))

# # 2.

# timestamp0_str = '30/03/09 16:31:32'
# b = datetime.strptime(timestamp0_str, '%d/%m/%y %H:%M:%S')
# print('type of b is:',type(b))
# print('b =',b)

# #3. 
# timestamp0_str = '30/03/09 16:31:32.097'
# c = datetime.strptime(timestamp0_str, '%d/%m/%y %H:%M:%S.%f')
# print('type of c is:',type(b))
# print('c =',c)

# #4. timestamp delta
# timestamp1_str = '30/04/09 10:30:27.017'
# d = datetime.strptime(timestamp1_str, '%d/%m/%y %H:%M:%S.%f')
# print('c = {0}, d = {1}'.format(c,d))
# print('time_delta = ', d-c)
# print('time_delta(seconds) = ', (d-c).total_seconds())

# #5. 
# timestamp2_str = '09-04-30 10:30:27'
# print('timestamp2 = ',datetime.strptime(timestamp2_str, '%y-%m-%d %H:%M:%S'))
# timestamp3_str = '2009-04-30 10:30:27'
# print('timestamp3 = ',datetime.strptime(timestamp3_str, '%Y-%m-%d %H:%M:%S'))
# # print('timestamp3 = ',datetime.strptime(timestamp3_str, '%y-%m-%d %H:%M:%S'))

# timestamp4_str = '19-04-30 10:30:27.067'
# print('timestamp4 = ',datetime.strptime(timestamp4_str, '%y-%m-%d %H:%M:%S.%f'))
# timestamp5_str = '2019-04-30 10:30:27.067'
# print('timestamp5 = ',datetime.strptime(timestamp5_str, '%Y-%m-%d %H:%M:%S.%f'))

# #6. 已知秒单位的时间戳，如何换算成年、月、日...的形式表示呢
# t1_secs = 11257868
# t1 = time.localtime(t1_secs)
# t1 = time.strftime('%Y-%m-%d %H:%M:%S',t1)
# t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
# print(t1)

# #7. (6)的方法只适用于精度到秒级的时间戳。由于time模块不支持到毫秒的精度，
# #   所以时间戳含毫秒的话，就无能为力了。那有没有什么办法解决呢？

