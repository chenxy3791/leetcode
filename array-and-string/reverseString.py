"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    #def reverseString(self, s: List[str]) -> None:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        sLen = len(s);
        if sLen == 0 or sLen == 1:
            return
        
        i = 0;
        j = sLen - 1;
        while i<j:
            #print(i,j)
            tmp  = s[i]
            s[i] = s[j]
            s[j] = tmp
            #print(s)
            i = i + 1
            j = j - 1

        return

#Reference Solution provided by leetcode.cn
#Python3    
#class Solution:
#    def reverseString(self, s):
#        """
#        :type s: List[str]
#        :rtype: void Do not return anything, modify s in-place instead.
#        """
#        def helper(start, end, ls):
#            if start >= end:
#                return
#        
#            # swap the first and last element
#            ls[start], ls[end] = ls[end], ls[start]        
#
#            return helper(start+1, end-1, ls)
#    
#        helper(0, len(s)-1, s)    

if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = []
    sln.reverseString(s)
    print(s)


    # Testcase1
    print('Testcase1...')
    s = ["h","e","l","l","o"]
    sln.reverseString(s)
    print(s)

    # Testcase2
    print('Testcase2...')
    s = ["H","a","n","n","a","h"]
    sln.reverseString(s)
    print(s)
    