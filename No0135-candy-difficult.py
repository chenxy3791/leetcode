# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 23:14:14 2022

@author: Dell
"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        N = len(ratings)
        flags = N * [0]
        
        for k in range(len(ratings)):
            if k==0:
                if ratings[0] > ratings[1]:
                    flags[0] = 1
                elif ratings[0] == ratings[1]:
                    flags[0] = -1
                else:
                    flags[0] = 0
                continue
            if k==N-1:
                if ratings[N-1] > ratings[N-2]:
                    flags[N-1] = 1
                elif ratings[N-1] == ratings[N-2]:
                    flags[N-1] = -1
                else:
                    flags[N-1] = 0
                continue
            if ratings[k-1]==ratings[k] and ratings[k+1]==ratings[k]:
                flags[k] = -1
            elif ratings[k-1]<ratings[k] and ratings[k+1]<ratings[k]:
                flags[k] = 1
            elif ratings[k-1]>ratings[k] and ratings[k+1]>ratings[k]:
                flags[k] = 0
            elif ratings[k-1]>ratings[k] and ratings[k+1]==ratings[k]:
                flags[k] = 0
            elif ratings[k-1]<ratings[k] and ratings[k+1]==ratings[k]:
                flags[k] = 1
            elif ratings[k-1]==ratings[k] and ratings[k+1]>ratings[k]:
                flags[k] = 0
            elif ratings[k-1]==ratings[k] and ratings[k+1]<ratings[k]:
                flags[k] = 1
            else:
                flags[k] = 2
        # print(flags)
        nums = len(ratings) * [0]
        for k in range(len(ratings)):
            if flags[k] == -1:
                nums[k] = 1
            elif flags[k] == 0:
                nums[k] = 1
                # backward search
                j = k-1
                while j>=0:
                    # print(j,flags[j])
                    if flags[j]==-1 or flags[j]==0:
                        break
                    elif flags[j]!=1:
                        nums[j] = nums[j+1]+1
                        j = j-1
                    else:
                        nums[j] = nums[j+1]+1 if nums[j+1]+1>nums[j] else nums[j]
                        break
                # forward search
                j = k+1
                while j<N:
                    if flags[j]==-1 or flags[j]==0:
                        break
                    elif flags[j]!=1:
                        nums[j] = nums[j-1]+1
                        j = j+1
                    else:
                        nums[j] = nums[j-1]+1 if nums[j-1]+1>nums[j] else nums[j]
                        break
                # print(k,nums)
        # print(nums)
        return sum(nums)
    
if __name__ == "__main__":
    
    sln = Solution()    
    
    ratings = [0]
    print(sln.candy(ratings))

    ratings = [1,0]
    print(sln.candy(ratings))

    # ratings = [1,0,2]
    # print(sln.candy(ratings))
    
    # ratings = [1,2,2]
    # print(sln.candy(ratings))
    
    # ratings = [1,2,2,2,2,2,3,2,2,2]
    # print(sln.candy(ratings))
    
    # ratings = [1,2,3,4,5,4,3,2,1,1]
    # print(sln.candy(ratings))
    
    ratings = [1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
    print(sln.candy(ratings))