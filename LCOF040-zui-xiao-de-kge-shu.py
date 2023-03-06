""" 
<<剑指Offer(第2版)>>
面试题40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

解题思路：
输入数组中的数如果有重复的话，在输出中也重复地算还是不能重复地算？
假定不能吧。。。-->以下题解是按这个理解
从题解来看，是含重复的。。。fuck! 

"""
import math
import time
import random
import string
import numpy as np

class Solution:
    #def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    def getLeastNumbers(self, arr, k: int):
        if len(arr) == 0 or k == 0:
            return []

        arr.sort()
        #print('arr after sorting: {0}'.format(arr))
        cnt  = 0
        rslt = []
        for kkk in range(len(arr)):
            if kkk == 0 or arr[kkk] != arr[kkk-1]:
                cnt += 1
                rslt.append(arr[kkk])
                if cnt == k:
                    break
            #print('kkk = {0}, cnt = {1}'.format(kkk,cnt))
        if cnt < k:
            return []
        else:
            return rslt
                                                           
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    arr = [3,2,1]
    k = 2
    tStart= time.time()
    print(sln.getLeastNumbers(arr,k))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))

    print('\ntestcase2 ...')
    arr = [0,1,2,1]
    k = 1
    tStart= time.time()
    print(sln.getLeastNumbers(arr,k))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))

    print('\ntestcase3 ...')
    arr = [0,1,2,1,3,2,3,2,4,5,6]
    k = 3
    tStart= time.time()
    print(sln.getLeastNumbers(arr,k))
    tStop = time.time()
    print('tElapsed={0}(sec)'.format(tStop-tStart))    
