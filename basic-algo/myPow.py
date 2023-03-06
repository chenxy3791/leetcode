"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

class Solution:
    def myPowNaive(self, x: float, n: int) -> float:
        print('n = {0}'.format(n))
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 0:
            return 0
        
        if n < 0:
            sign = 1
            n    = -n
        else:
            sign = 0
        
        n1 = int(n/2)
        n2 = n - n1

        rslt = self.myPow(x,n1) * self.myPow(x,n2)
        return rslt if sign == 0 else 1.0/rslt

    def myPow(self, x: float, n: int) -> float:
        print('n = {0}'.format(n))

        def helper(m, memo):
            tmp = memo.get(m)
            if tmp != None:
                return tmp

            if m == 0:
                return 1
            if m == 1:
                return x
            if x == 0:
                return 0

            m1   = int(m/2)
            m2   = m - m1
            rslt = helper(m1,memo) * helper(m2,memo)
            memo[m] = rslt
            return rslt

        if n < 0:
            sign = 1
            n    = -n
        else:
            sign = 0
        
        memo = dict()
        rslt = helper(n, memo)
        return rslt if sign == 0 else 1.0/rslt


if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    x = 2.0
    n = 10
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase2...')
    x = 2.1
    n = 3
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase3...')
    x = 2.00000
    n = -2
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase4...')
    x = 0.00000
    n = 20197
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase5...')
    x = 3.00000
    n = 20
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase6...')
    x = 0.9
    n = 2**31 - 1
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase7...')
    x = 609763.00000
    n = -2**32
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))

    print('Testcase8...')
    x = 609763.00000
    n = 0
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))    

    print('Testcase9...')
    x = 0
    n = 0
    print('x = {0}, n = {1}, Expected = {2}; result = {3}'.format(x, n, x**n, sln.myPow(x,n)))    
