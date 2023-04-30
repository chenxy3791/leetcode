# -*- coding: utf-8 -*-
"""
Created on Thu May 26 19:33:13 2022

@author: Dell
"""

# =============================================================================
# 描述
# map() 会根据提供的函数对指定序列做映射。
# Python 的 map()函数作用于一个可迭代对象，使用一个函数，并且将函数应用于这个可迭代对象的每一个元素。
# 
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
# 
# 语法
# map() 函数语法：
# map(function, iterable, ...)
# 参数
# function -- 函数
# iterable -- 一个或多个序列
# 返回值
# Python 2.x 返回列表。
# Python 3.x 返回迭代器。
# =============================================================================

def square(x) :         # 计算平方数
    return x ** 2

a = map(square, [1,2,3,4,5])    # 计算列表各个元素的平方
print(a)

b = list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
print(b)

print(list(map(lambda x: x ** 2, list(range(10)))))   # 使用 lambda 匿名函数

# =============================================================================
# 假如我们有一个字符串列表，我们想要将每一个元素都转换成大写字母。
# 
# 想要实现这个目的的一种方式是，使用传统的for循环:
# =============================================================================

directions = ["north", "east", "south", "west"]
directions_upper = []
 
for direction in directions:
    d = direction.upper()
    directions_upper.append(d)
print(directions_upper)

print(list(map(lambda x:x.upper(),directions)))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


# =============================================================================
# 一个 lambda 函数是一个小的匿名函数。
# 下面是另外一个例子，显示如何创建一个列表，从1到10。
# =============================================================================

squares = map(lambda n: n*n , range(1, 11))
print(list(squares))
# 基于列表推导实现map函数
print([k*k for k in range(1,11)])

# =============================================================================
# 二、对多个迭代对象使用map()
# 
# 你可以将任意多的可迭代对象传递给map()函数。回调函数接受的必填输入参数的数量，必须和可迭代对象的数量一致。
# 
# 下面的例子显示如何在两个列表上执行元素级别的操作：
# =============================================================================
a = [1, 4, 6]
b = [2, 3, 5]
result = map(lambda x,y: x*y, a, b)
print(list(result))

# =============================================================================
# 当提供多个可迭代对象时，返回对象的数量大小和最短的迭代对象的数量一致。
# 让我们看看一个例子，当可迭代对象的长度不一致时：
# 超过的元素 （7 和 8 ）被忽略了。
# =============================================================================
a = [1, 4, 6]
b = [2, 3, 5, 7, 8]
result = map(lambda x, y: x*y, a, b)
print(list(result))

a = [1, 4, 6]
b = [2, 3, 5, 7, 8]
c = [10,11,12]
print(list(map(lambda x,y,z:x+y+z, a,b,c)))

# =============================================================================
# Python映射多个函数
# 在以下示例中，我们将展示如何在 Python中使用map()映射多个函数。
# 我们遍历for循环中的元素。在每个循环中，我们创建一个包含两个值的列表，
# 这些结果是通过对传入参数应用add()和square()函数来计算的。
# =============================================================================
# 函数1
def add(x):
    return x + x
# 函数2
def square(x):
    return x * x
# 数据
nums = [1, 2, 3, 4, 5]

# 逐个取数处理
for i in nums:
    # lambda为处理函数，分别将add和square传给lambda
    vals = list(map(lambda x: x(i), (add, square)))
    print(vals)



# Function to replace a character c1 with c2 
# and c2 with c1 in a string S 
def replaceChars(input,c1,c2):
  
     # create lambda to replace c1 with c2, c2 
     # with c1 and other will remain same 
     # expression will be like "lambda x:
     # x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2"
     # and map it onto each character of string
     newChars = map(lambda x: x if (x!=c1 and x!=c2) else \
                c1 if (x==c2) else c2,input)
  
     # now join each character without space
     # to print resultant string
     print (''.join(newChars))
input = 'grrksfoegrrks'
c1 = 'e'
c2 = 'r'
replaceChars(input,c1,c2)


# Function to calculate sum of all elements in matrix
# sum(arr) is a python inbuilt function which calculates
# sum of each element in a iterable ( array, list etc ).
# map(sum,arr) applies a given function to each item of 
# an iterable and returns a list of the results.
def findSum(arr):
  
    # inner map function applies inbuilt function  
    # sum on each row of matrix arr and returns 
    # list of sum of elements of each row
    return sum(map(sum,arr))  

arr = [[1, 2, 3], [4, 5, 6], [2, 1, 2]]
print ("Sum = ",findSum(arr))

# Function to find sums of ASCII values of each
# word in a sentence in

def asciiSums(sentence):

	# split words separated by space
	words = sentence.split(' ')

	# create empty dictionary
	result = {}

	# calculate sum of ascii values of each word
	for word in words:
		currentSum = sum(map(ord,word))

		# map sum and word into resultant dictionary
		result[word] = currentSum

	totalSum = 0

	# iterate list of splited words in order to print
	# sum of ascii values of each word sequentially
	sumsOfAscii = [result[word] for word in words]
	print ('Sum of ASCII values:')
	print (' '.join(map(str,sumsOfAscii)))
	print ('Total Sum -> ',sum(sumsOfAscii))

# Driver program
if __name__ == "__main__":
	sentence = 'I am a geek'
	asciiSums(sentence)

# =============================================================================
# How to Map a Function Over NumPy Array?
# Method 1: numpy.vectorize() method
# The numpy.vectorize() function maps functions on data structures that contain 
# a sequence of objects like NumPy arrays. The nested sequence of objects or 
# NumPy arrays as inputs and returns a single NumPy array or a tuple of NumPy arrays.
# 
# =============================================================================
import numpy as np
  
arr = np.array([1, 2, 3, 4, 5])
  
def addTwo(i):
    return i+2
    
applyall = np.vectorize(addTwo)
res = applyall(arr)
print(res)

# =============================================================================
# Method 2: Using lambda function
# The lambda is an anonymous function, it takes any number of arguments but evaluates one expression.
# =============================================================================
arr = np.array([1, 2, 3, 4, 5])
print(list(map(lambda x:x+2, arr)))
# Method 3: Using an array as the parameter of a function to map over a NumPy array
# import numpy as np
  
arr = np.array([1, 2, 3, 4, 5])
  
def applyall(i): 
  return i + 2
  
res = applyall(arr)
print(res)