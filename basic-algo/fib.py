# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def fibCore(self, N: int, fibBuf: dict):
        if N == 0:
            fibBuf[N] = 0
            return 0,fibBuf
        if N == 1:
            fibBuf[N] = 1
            return 1,fibBuf
    
        fibPrev1 = fibBuf.get(N-1)
        if fibPrev1 == None:
            fibPrev1, fibBuf = self.fibCore((N-1), fibBuf)
            
        fibPrev2 = fibBuf.get(N-2)
        if fibPrev2 == None:
            fibPrev2, fibBuf = self.fibCore((N-2), fibBuf)

        fibCur = fibPrev1 + fibPrev2
        fibBuf[N] = fibCur

        return fibCur, fibBuf

    def fib(self, N: int) -> int:
        fibBuf = {}
        fibCur, fibBuf = self.fibCore(N, fibBuf)

        return fibCur

    def fib_ref(self, N):
        """
        :type N: int
        :rtype: int

        Reference solution give by leetcode. Tow points:
        [1] Check whether a key in a dictionary
        [2] Function definition in side a function
        """
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            # put result in cache for later reference.
            cache[N] = result
            return result

        return recur_fib(N)

if __name__ == "__main__":

    sln = Solution()
    for k in range(30):
        print('k = {0}, fib(k) = {1}'.format(k, sln.fib(k)))
            
    for k in range(30):
        print('k = {0}, fib(k) = {1}'.format(k, sln.fib_ref(k)))
        