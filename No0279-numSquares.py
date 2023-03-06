""" 
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9. 
"""
import math

class Solution:

    def isCompleteSquare(self,x: int):            
        if x == int(math.sqrt(x))**2:
            return True
        else:
            return False

    # def numSquaresDP(self, n: int) -> int:
    #     #RecursionError: maximum recursion depth exceeded while calling a Python object
    #     assert(n > 0) # n must be positive integer        

    #     cache = dict()
    #     def dp(m):                        
    #         if m in cache:
    #             print('dp({0})...return {1}'.format(m,cache[m]))
    #             return cache[m]         

    #         if self.isCompleteSquare(m):
    #             cache[m] = 1
    #             print('dp({0})...return {1}'.format(m,cache[m]))
    #             return 1
        
    #         minNum = n 
    #         #for x in range(2,int(math.sqrt(m))+1):
    #         x = 1
    #         while x**2 < m:
    #             y = dp(m-x**2) 
    #             if minNum > y:
    #                 minNum = y
    #             x = x + 1
    #         cache[m] = minNum + 1
    #         print('dp({0})...return {1}'.format(m,cache[m]))
    #         return cache[m]

    #     return dp(n)

    def numSquaresSlow(self, n: int) -> int:
        assert(n > 0) # n must be positive integer        
        # In this problem, no vivisted buffer is needed.
        # cache = dict()
        q = [n]
        layer = -1
        while len(q) > 0:
            qSize = len(q)
            layer = layer + 1
            print('layer = {0}'.format(layer))
            # print('layer = {0}, q = {1}'.format(layer,q))
            # print(q, visited)
            for k in range(qSize):
                a = q.pop(0)
                #visited.append(a)
                if a == 0:
                    return layer
                else: # Add a's neighbours into q
                    # if a in cache:
                    #     lstSqu = cache[a]
                    # else:
                    #     lstSqu = completeSquares(a)
                    # cache[a] = lstSqu    
                    if a < 4:
                        q.append((a-1)) # No other choices except 1
                    else:
                        for x in range(1,int(math.sqrt(a))):
                            q.append(a-(x+1)**2) # Note: push the residue to queue.

    def numSquares(self, n: int) -> int:
        """ Time: Win 45.14% of python3 submission"""
        """ Memory: Win 5.74% of python3 submission"""
        assert(n > 0) # n must be positive integer        
        # In this problem, no vivisted buffer is needed.
        # cache = dict()
        q = [n]
        layer = -1
        while len(q) > 0:
            qSize = len(q)
            layer = layer + 1
            # print('layer = {0}'.format(layer))
            # print('layer = {0}, q = {1}'.format(layer,q))            
            for k in range(qSize):
                a = q.pop(0)
                #visited.append(a)
                if a == 0:
                    return layer
                elif self.isCompleteSquare(a):
                    print(a)
                    return layer + 1
                else: # Add a's neighbours into q
                    # x = 1
                    # while x**2 < a:
                    #     q.append(a-x**2)
                    #     x = x + 1                    
                    x = int(math.sqrt(a))
                    while x > 0:
                        q.append(a-x**2)
                        x = x - 1        

if __name__ == '__main__':

    import time
    sln   = Solution()

    # # testcase0    
    # print('sln.numSquares(1)  = {0}'.format(sln.numSquares(1)))
    # print('sln.numSquares(4)  = {0}'.format(sln.numSquares(4)))
    # print('sln.numSquares(9)  = {0}'.format(sln.numSquares(9)))
    # print('sln.numSquares(16) = {0}'.format(sln.numSquares(16)))

    # testcase1
    n = 12
    print('sln.numSquares({0}) = {1}'.format(n,sln.numSquares(n)))

    # testcase2
    n = 13
    print('sln.numSquares({0}) = {1}'.format(n,sln.numSquares(n)))

    # testcase3
    tStart = time.time()    
    n = 1268
    print('sln.numSquares({0}) = {1}'.format(n,sln.numSquares(n)))    
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # testcase4
    tStart = time.time()    
    n = 7168
    print('sln.numSquares({0}) = {1}'.format(n,sln.numSquares(n)))    
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
