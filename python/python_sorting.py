# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:48:48 2022

@author: Dell
"""
# 1. sorting basic
# 1.1 ascending sort
print(sorted([5, 2, 3, 1, 4]))

print([5, 2, 3, 1, 4].sort()) # NG!

a = [5, 2, 3, 1, 4]
a.sort()
print(a)

# 1.2 descending sort
print(sorted([5, 2, 3, 1, 4],reverse=True))
a = [5, 2, 3, 1, 4]
a.sort(reverse=True)
print(a)

# 2. Key Functions
a = sorted("This is a test string from Andrew".split())
b = sorted("This is a test string from Andrew".split(), key=str.lower)
print(a)
print(b)

test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]

# using sort() + lambda
# to sort list of list 
# sort by second index
a = sorted(test_list, key = lambda test_list: test_list[0])
b = sorted(test_list, key = lambda test_list: test_list[1])
c = sorted(test_list, key = lambda test_list: test_list[2])
print(a)
print(b)
print(c)

from operator import itemgetter
d = sorted(test_list, key = itemgetter(2))
# printing result
print ("List after sorting by 2nd element of lists : " + str(d))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print(sorted(student_objects, key=lambda student: student.age))

# 3. Returning index of a sorted list
# 3.1 Method 1
# numpy.argsort() function is used to perform an indirect sort along the given 
# axis using the algorithm specified by the kind keyword. 
# It returns an array of indices of the same shape as arr that that would sort the array.
import numpy
s = numpy.array([2, 3, 1, 4, 5])
sort_index = numpy.argsort(s)
print(list(sort_index))

# 3.2 Method 2
s = [2, 3, 1, 4, 5]
li=[]

for i in range(len(s)):
	li.append([s[i],i])
li.sort()
sort_index = []

for x in li:
	sort_index.append(x[1])

print(sort_index)

