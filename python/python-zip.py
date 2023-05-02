# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:10:48 2021

@author: chenxy
"""

weekdays = ['Monday','Wendsday','Tuesday','Thursday','Friday','Saturday','Sunday']
for wd in weekdays:
    print(wd,end=', ')
print('\n')    
for k in range(len(weekdays)):
    print(weekdays[k],end=', ')    
    
print('\n')        

weekdays = ['Monday','Wendsday','Tuesday','Thursday','Friday','Saturday','Sunday']
weekdays_chinese = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日' ]
for k in range(len(weekdays)):
    print(weekdays[k],' --> ', weekdays_chinese[k])    

print('\n')        
weekdays = ['Monday','Wendsday','Tuesday','Thursday','Friday','Saturday','Sunday']
weekdays_chinese = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六' ]    
min_len = min(len(weekdays),len(weekdays_chinese))
for k in range(min_len):
    print(weekdays[k],' --> ', weekdays_chinese[k])    

print('\n')            
weekdays = ['Monday','Wendsday','Tuesday','Thursday','Friday','Saturday','Sunday']
weekdays_chinese = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日' ]  
zipPair = zip(weekdays, weekdays_chinese)
print(zipPair)
print(list(zipPair))

weekdays = ['Monday','Wendsday','Tuesday','Thursday','Friday','Saturday','Sunday']
weekdays_chinese = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日' ]  
weekdays_japanese = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日','日曜日' ]
zipTriple = zip(weekdays, weekdays_chinese, weekdays_japanese)
print(list(zipTriple))

print('\n')   
a = [1,2,3,4,5]
print(list(zip(a)))
print(list(zip()))

print('\n')   
zipTriple = zip(weekdays, weekdays_chinese, weekdays_japanese)
wk1, wk2, wk3 = zip(*zipTriple)
print(wk1)
print(wk2)
print(wk3)

print('\n')   
import itertools as it
fruits = ['apple', 'banana', 'melon', 'strawberry']
prices = [10, 20, 30]
print(list(it.zip_longest(fruits, prices)))

print('\n')   
import itertools as it
fruits = ['apple', 'banana', 'melon', 'strawberry']
prices = [10, 20, 30]
print(list(it.zip_longest(fruits, prices, fillvalue='Sold out')))