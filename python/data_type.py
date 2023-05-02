# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 15:43:03 2022

@author: chenxy
"""

# 初始化一个空的字典
d = {} 
# d = dict()
# 给字典追加条目或者更新其中的条目
d['name'] = 'alice'
d['sex']  = 'female'
d['age']  = 13
d['nationality'] = 'USA'

# 直接用key-value pairs进行字典初始化，与上面的写法等价，但是这个显然更加简洁
# d = dict(name='alice', sex='female', age=13, nationality='USA')
print(d)
print(d.keys())
print(d.values())

# 读取其中某个key所对应的值。要注意的是在上面初始化时name等是不加引号的, 会被自动识别为字符串
print(d['name'])

# 也许正因为此，以下这种基于key-value pair的初始化是不行的。虽然以数值为key本身是可以的
# d2 = dict(1 = 'bob')   # NG
d[1] = 'bob'             # OK
d[1.1] = 'tom'           # OK
print(d[1.1])


# 集合的初始化
s1 = {1,2,3}
s2 = set([1,2,3])
print(s1,s2)


k1 = 1
k2 = 123456781234567812345678
x1 = 1.2
print(type(k1),type(k2),type(x1))
# print(type(k1),type(k2),type(x1),type(x2))
c = 'a'
a = []
b = ()
d = {}
s = {1}

print('type(1) = ', type(1))
print('type(a) = ', type(a))
print('type(b) = ', type(b))
print('type(c) = ', type(c))
print('type(d) = ', type(d))
print('type(s) = ', type(s))


print(isinstance(k1, int))
print(isinstance(x1, float))
print(isinstance(a, list))
print(isinstance(b, tuple))
print(isinstance(c, str))
print(isinstance(d, dict))
print(isinstance(s, set))

print()
print("str.is***() family examples:")

print('abc'.isalpha())
print('1'.isalnum())
print('ab1'.isalpha())
print('ab1'.isalnum())
print(' '.isspace())
print('123'.isalnum())
print('123'.isnumeric())
print('1.3'.isnumeric())
print('123'.isdecimal())
print('a'.islower())
print('A'.isupper())
