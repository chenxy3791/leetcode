""" 
365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False

"""
import math
import time
import numpy as np

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
                           
if __name__ == '__main__':


    sln   = Solution()

    print('\ntestcase1 ...')
    x = 3
    y = 5
    z = 4
    tStart= time.time()
    print(sln.canMeasureWater(x,y,z))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    x = 2
    y = 6
    z = 5
    tStart= time.time()
    print(sln.canMeasureWater(x,y,z))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        


