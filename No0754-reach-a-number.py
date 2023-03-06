# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:45:20 2022

@author: chenxy
"""
import time
from typing import List	

class Solution:
    def reachNumber_dp(self, target: int) -> int:
        memo = dict()
        def dp(i, cur_target):            
            print('dp({0},{1}) ...'.format(i,cur_target))
            if i == 5: # for debug only
                return 0
            if cur_target == 0:
                return 0

            if (i,cur_target) in memo:
                return memo[(i, cur_target)]
            
            ret = min(dp(i+1, cur_target-i), dp(i+1, cur_target+i))
            memo[(i, cur_target)] = ret
            return ret

        return dp(1, target)
    def reachNumber_bfs(self, target: int) -> int:
        
        
if __name__ == '__main__':       
    
    sln = Solution()    
        
    tStart = time.time()        
    target = 2
    ans = sln.reachNumbe_dpr(target)
    tElapsed = time.time() - tStart            
    print('target={0}, ans={1}, tCost={2:3.2f}(sec)'.format(target,ans,tElapsed))        