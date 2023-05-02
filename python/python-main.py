# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:45:17 2021

@author: chenxy
"""

print("first")
 
 
def sayHello():
    str = "hello"
    print(str);
    print(__name__+'from hello.sayhello()')
 
 
if __name__ == "__main__":
    print ('This is main of module "hello.py"')
    sayHello()
    print(__name__+'from hello.main')