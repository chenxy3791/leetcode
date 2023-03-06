""" 
1013. Partition Array Into Three Parts With Equal Sum
Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4
"""
"""
解题思路1：
注意，分组是按照原有顺序，相邻的元素构成一组。相当于从数组中切两刀分成三组，
而不是任意三组。
"""
class Solution:
    #def canThreePartsEqualSum(self, A: List[int]) -> bool:
    def canThreePartsEqualSum(self, A) -> bool:
        if len(A) < 3:
            return False
        totalsum = sum(A)
        if (totalsum % 3) != 0:
            return False
        
        target = totalsum/3

        k = 0
        runsum = 0
        grpcnt = 0
        while k < len(A):
            runsum += A[k]
            if runsum == target:
                runsum = 0
                grpcnt = grpcnt + 1
                if grpcnt==3:
                    if k==len(A)-1:
                        return True
                    else:
                        if sum(A[k+1:])==0:
                            return True
                        else:
                            return False
            k += 1

        return False
        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase1 ...')
    A = [0,2,1,-6,6,-7,9,1,2,0,1]
    print(sln.canThreePartsEqualSum(A))

    print('\nTestcase2 ...')
    A = [0,2,1,-6,6,7,9,-1,2,0,1]
    print(sln.canThreePartsEqualSum(A))    

    print('\nTestcase3 ...')
    A = [3,3,6,5,-2,2,5,1,-9,4]
    print(sln.canThreePartsEqualSum(A))    