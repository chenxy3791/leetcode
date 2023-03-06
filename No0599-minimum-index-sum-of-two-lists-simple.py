# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 08:13:01 2022

@author: chenxy

599. 两个列表的最小索引总和
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 
如果答案不止一个，则输出所有答案并且不考虑顺序。 
你可以假设答案总是存在。
 
示例 1:
输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”

示例 2:
输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。

提示:
1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30 
list1[i] 和 list2[i] 由空格 ' ' 和英文字母组成。
list1 的所有字符串都是 唯一 的。
list2 中的所有字符串都是 唯一 的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it
# import numpy as np
class Solution:
    def findRestaurant1(self, list1: List[str], list2: List[str]) -> List[str]:
        idxsum = len(list1) + len(list2)      
        ans    = []
        for k1,item1 in enumerate(list1):
            print(k1,item1)
            for k2, item2 in enumerate(list2):
                if item1 == item2:
                    if idxsum > k1+k2:
                        idxsum = k1+k2
                        ans    = [item1]
                    elif idxsum == k1+k2:
                        ans.append(item1)
                    break                                        
        return ans

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index2 = {item: k for k, item in enumerate(list2)}
        
        idxsum = float('inf')
        ans    = []
        for k1,item1 in enumerate(list1):            
            if item1 in index2:  
                k2 = index2[item1]
                if idxsum > k1+k2:
                    idxsum = k1+k2
                    ans    = [item1]
                elif idxsum == k1+k2:
                    ans.append(item1)                        
        return ans
    
if __name__ == '__main__':            
    
    sln = Solution()

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    tStart = time.time()        
    ans = sln.findRestaurant(list1,list2)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))         

    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]     
    tStart = time.time()        
    ans = sln.findRestaurant(list1,list2)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))            
    
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    tStart = time.time()        
    ans = sln.findRestaurant(list1,list2)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))                