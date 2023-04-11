# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 07:59:44 2022

@author: Dell
"""
from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfDividing(num):
            num0 = num # bakup
            if num < 10:
                return True
            while num > 0:
                # print(num)
                tmp = num % 10
                if tmp == 0:
                    return False
                if num0 % tmp !=0:
                    return False
                num = num // 10
            return True
        ans = []
        for k in range(left, right+1):
            if selfDividing(k):
                ans.append(k)
        return ans

if __name__ == '__main__':
    
    sln = Solution()
    print(sln.selfDividingNumbers(1, 22))
    print(sln.selfDividingNumbers(47, 85))
            