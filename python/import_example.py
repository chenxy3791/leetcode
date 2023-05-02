# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 12:19:45 2021

@author: chenxy
"""

# import math

# # 用math库中的函数和常量进行运算
# math.sqrt(math.pi)

# # 可以不导入完整的模块，而只导入其中的某些部件（类、函数、常量等）。可以同时导入多个，用逗号分隔
# from math import sqrt, pi
# # 这样导入后不需要前缀，可以直接使用
# sqrt(pi)

# # 还可以在导入时给module起一个昵称，以方便使用。比如说
# import numpy as np
# np.sqrt(np.pi)

# from numpy import *
# print(sqrt(pi))

# from math import sqrt as math_sqrt
# from numpy import sqrt as np_sqrt
# from math import radians as rad   # given the function radians an alias `rad`
# print('math_sqrt(math.pi) = {0}, np_sqrt(np.pi) = {1}'.format(math_sqrt(math.pi),np_sqrt(np.pi)))
# print('rad(180) =', rad(180))

# package不能单独地导入?
# import package_example
# package_example.HelloModule.HelloWorldFunc()

# # Import modules from a package -- method#1
import package_example.HelloModule
# import package_example.HelloModule as myHelloModule
# from   package_example import HelloModule
# from   package_example import *
package_example.HelloModule.HelloWorldFunc()
helloClassObj = package_example.HelloModule.HelloWorldClass()
helloClassObj.helloWorld()

# # import package_example.HelloModule as myHelloModule
# # myHelloModule.HelloWorldFunc()


# from package_example import HelloModule
# # from package_example import *
# HelloModule.HelloWorldFunc()






