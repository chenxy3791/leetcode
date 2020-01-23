""" 
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""

import time
import math

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

k = 11

def isBadVersion(version):
    """
    A dummy implementation for the convenience of debug
    k is global variable, represent the ground-truth
    """

    if version >= k:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int -- NOTE: 1-indexed!
        """
        ptr      = int(n/2) # start from the middle point
        step     = max(1, math.ceil(n/4))
        prevIdx  = n
        prevRslt = None
        while(1):
            #print('ptr = {0}, step = {1}'.format(ptr,step))
            if isBadVersion(ptr) is False:
                #print('False')
                #Termination judge
                if (prevRslt is True) and (prevIdx == (ptr+1)):
                    return prevIdx

                prevIdx = ptr
                prevRslt= False
                ptr    += step
            else:
                #print('True')
                #Termination judge                
                if ptr == 1:
                    return 1
                if (prevRslt is False) and (prevIdx == (ptr-1)):
                    return ptr

                prevIdx = ptr
                prevRslt= True
                ptr    -= step
            step = max(1, math.ceil(step/2))
            if ptr > n:
                return None

        # Passed the while-loop without early-termination?
        # Not consider this kind of case

                
if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    print('Testcase1...')
    n = 11
    # k = 10 # Defined above as gloabal variable!
    print(sln.firstBadVersion(n))

