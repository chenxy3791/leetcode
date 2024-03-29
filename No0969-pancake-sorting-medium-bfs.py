# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 09:02:59 2022

@author: chenxy

969. 煎饼排序
给你一个整数数组 arr ，请使用 煎饼翻转 完成对数组的排序。一次煎饼翻转的执行过程如下：

选择一个整数 k ，1 <= k <= arr.length
反转子数组 arr[0...k-1]（下标从 0 开始）
例如，arr = [3,2,1,4] ，选择 k = 3 进行一次煎饼翻转，反转子数组 [3,2,1] ，得到 arr = [1,2,3,4] 。

以数组形式返回能使 arr 有序的煎饼翻转操作所对应的 k 值序列。任何将数组排序且翻转次数在 10 * arr.length 范围内的有效答案都将被判断为正确。

示例 1：
输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。 

示例 2：
输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。
 
提示：
1 <= arr.length <= 100
1 <= arr[i] <= arr.length
arr 中的所有整数互不相同（即，arr 是从 1 到 arr.length 整数的一个排列）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pancake-sorting
"""
from typing import List
from   collections import deque
import time

class Solution:    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(card, k):
            new_card = card.copy()
            for l in range(k//2):
                new_card[l], new_card[k-1-l] = new_card[k-1-l], new_card[l]
            return new_card
        
        visited = dict() # Store visited nodes accompanied with k leading to them, for later recovering the whole sequence
        
        target  = tuple([m+1 for m in range(len(arr))])
        # print(target)

        q = deque()        
        q.append((arr,0))
        visited[tuple(arr)] = None
         
        while len(q) > 0 :
            node, layer = q.popleft()
            # print(node,layer)
            if layer > 10*len(arr):
                return None # Indicated failure
            if tuple(node) == target:
                # recover the whole operation sequence, with back-tracing
                path = []               
                k = visited[tuple(node)]
                while k != None:
                    path.insert(0,k)
                    node = flip(node,k) # flipping is invertible operation.
                    k = visited[tuple(node)]
                    # print(node,k, path)
                return path
            
            for k in range(2,1+len(arr)): #遍历邻节点, Note: 1 means no flipping!
                new_node = flip(node,k)
                if tuple(new_node) not in visited:
                    # Add k to path, and add new_card to visited
                    visited[tuple(new_node)] = k                    
                    q.append((new_node,layer+1))                
        return None # Indicated failure

if __name__ == '__main__':        
    
    sln = Solution()

    # card = [3,2,4,1]
    # print(sln.pancakeSort(card))

    # card = [1,2,3]
    # print(sln.pancakeSort(card))                    
        
    # card = [1,2,5,3,4]
    # tStart = time.time()
    # print(sln.pancakeSort(card))                    
    # tCost = time.time() - tStart
    # print('card = {0}, tCost = {1}(sec)'.format(card,tCost))    
    
    # testcase: 156 / 215
    card = [1,10,3,7,4,8,2,5,9,6]
    tStart = time.time()
    print(sln.pancakeSort(card))                    
    tCost = time.time() - tStart
    print('card = {0}, tCost = {1}(sec)'.format(card,tCost))    
    