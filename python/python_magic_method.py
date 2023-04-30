# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:30:59 2022

@author: Dell
"""
# 以下代码使用魔术方法，采用运算符重载的方式实现了向量的加减法操作
class Vector:
    a = None
    b = None
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector(%d, %d)'  % (self.a, self.b)
    def __add__ (self, other):
        return Vector(self.a + other.a, self.b + other.b)
    def  __sub__(self, other):
        return Vector(self.a - other.a, self.b - other.b)

if __name__ == "__main__":

    v1 = Vector(1, 2)
    v2 = Vector(3, 4 )
    print(v1, " + ", v2, "=", v1 + v2)
    print(v1, " - ", v2, "=", v1 - v2)