# -*- coding: utf-8 -*-
"""
Spyder Editor

chenxy, 2021-03-7.

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

2021-03-08 
执行结果：通过
显示详情
执行用时：232 ms, 在所有 Python3 提交中击败了13.20%的用户
内存消耗：28.6 MB, 在所有 Python3 提交中击败了77.85%的用户

"""

class Solution:
    def isPalindrome(self, s: str):
        n = len(s)
        
        for k in range(n//2):
            if s[k] != s[n-k-1]:            
                return False
        return True
                                        
    def partition(self, s: str):
        n = len(s)
        #print('n = ', n)
        if n == 0:
            return []
        listOfPartition = []
        for l in range(1, n+1): # loop for 0-start palindrome
            #print('l = ', l)
            if self.isPalindrome(s[:l]):   
                curPartition = []
                curPartition.append(s[:l])                                
                if l == n:
                    #curPartition.append(s[:l])
                    listOfPartition.append(curPartition)
                else:
                    sub_rslt = self.partition(s[l:])
                    #print(s[:l], ':', sub_rslt)
                    #curPartition.append(s[:l])                        
                    for k in range(len(sub_rslt)):                        
                        listOfPartition.append(curPartition + sub_rslt[k])
                
        return listOfPartition
                    
if __name__ == '__main__':        
    #import time
    sln = Solution()
    
    s = 'a'
    print(sln.partition(s))
    
    s = 'aab'
    print(sln.partition(s))

    s = 'cdd'
    print(sln.partition(s))

#    s = 'abacaba'
#    print(sln.partition(s))
#    
#    s = 'aaabbbc'
#    print(sln.partition(s))
