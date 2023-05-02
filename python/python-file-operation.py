# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:30:57 2021

@author: chenxy
"""

f= open("myfile.txt","w+")
for i in range(4):
     f.write("This is line %d\n" % (i+1))
f.close()

f= open("myfile2.txt","w")
for i in range(4):
     f.write("This is line %d\n" % (i+1))
f.close()

f= open("myfile.txt","w+")
for i in range(4):
     f.write("This is line %d\n" % (i+1))
f.close()

f= open("myfile2.txt","w")
for i in range(4):
     f.write("This is line %d\n" % (i+1))
f.close()

f= open("myfile.txt","a+")
for i in range(4):
     f.write("Appended line %d\n" % (i+1))
f.close()

f=open('myfile.txt','r')
if f.mode == 'r':
    contents = f.read()
    print(contents)
f.close()

print('Read line by line...')
f=open('myfile.txt','r')
if f.mode == 'r':
    f_lines = f.readlines()
    print(type(f_lines))
    print(f_lines)
    for line in f_lines:
        print(line)
f.close()