# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 08:21:00 2023

@author: chenxy
2469. 温度转换
给你一个四舍五入到两位小数的非负浮点数 celsius 来表示温度，以 摄氏度（Celsius）为单位。

你需要将摄氏度转换为 开氏度（Kelvin）和 华氏度（Fahrenheit），并以数组 ans = [kelvin, fahrenheit] 的形式返回结果。

返回数组 ans 。与实际答案误差不超过 10-5 的会视为正确答案。

注意：

开氏度 = 摄氏度 + 273.15
华氏度 = 摄氏度 * 1.80 + 32.00
 

示例 1 ：

输入：celsius = 36.50
输出：[309.65000,97.70000]
解释：36.50 摄氏度：转换为开氏度是 309.65 ，转换为华氏度是 97.70 。
示例 2 ：

输入：celsius = 122.11
输出：[395.26000,251.79800]
解释：122.11 摄氏度：转换为开氏度是 395.26 ，转换为华氏度是 251.798 。
 

提示：0 <= celsius <= 1000
"""
import time
import random
from typing import List	
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
import bisect

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15, 9*celsius/5+32]
        

if __name__ == '__main__':

    sln  = Solution()                
    
    celsius = 36.50
    print(sln.convertTemperature(celsius))
        
    celsius = 122.11
    print(sln.convertTemperature(celsius))