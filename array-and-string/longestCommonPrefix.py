""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

import time

class Solution:
    #def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, strs) -> str:
        nStrs = len(strs)
        if nStrs == 0:
            return ""
        if nStrs == 1:
            return strs[0]

        strLen = [len(item) for item in strs]
        minLen = min(strLen)

        misMatch = False
        for k in range(0,minLen):
            for j in range(1,nStrs): # Always using strs[0] as the reference for comparison
                if strs[j][k] != strs[0][k]:
                    misMatch = True
                    break
            
            if misMatch:
                break
        if misMatch:
            return strs[0][0:k]
        else:
            return strs[0][0:minLen]

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('\nTestcase0...')
    strs = []
    print(strs, '--> ', sln.longestCommonPrefix(strs))

    strs = [[]]
    print(strs, '--> ', sln.longestCommonPrefix(strs))

    # Testcase1
    print('\nTestcase1...')
    strs = ["flower","flow","flight"]
    print(strs, '--> ', sln.longestCommonPrefix(strs))

    # Testcase2
    print('\nTestcase2...')
    strs = ["dog","racecar","car"]
    print(strs, '--> ', sln.longestCommonPrefix(strs))

    # Testcase3
    print('\nTestcase3...')
    strs = ["dog","dogcar","dogcarrace"]
    print(strs, '--> ', sln.longestCommonPrefix(strs))

    # Testcase4
    print('\nTestcase3...')
    strs = ["aa","a"]
    print(strs, '--> ', sln.longestCommonPrefix(strs))