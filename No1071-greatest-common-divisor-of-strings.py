""" 
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
Return the largest string X such that X divides str1 and X divides str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
如果有非空gcd-str的话，较短的那个一定是较长的那个的子串
如果有非空gcd-str的话，gcd_str的长度一定是两者长度的gcd
可以模仿求gcd的辗转相除法
"""
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        if len1 == 0 or len2 == 0:
            return ""

        if len1 >= len2:
            lstr = str1
            sstr = str2
        else:
            lstr = str2
            sstr = str1
        
        k = lstr.find(sstr)
        # print('str1 = {0}, str2 = {1}, k = {2}'.format(str1,str2,k))
        if k != 0:
            return ""
        if len1 == len2:
            return sstr

        gcdstr = self.gcdOfStrings(lstr[len(sstr):],sstr)

        return gcdstr
                           
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()

    print('\ntestcase1 ...')
    str1 = "ABCABC"
    str2 = "ABC"
    tStart= time.time()
    print(sln.gcdOfStrings(str1, str2))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    str1 = "ABABAB"
    str2 = "ABAB"
    tStart= time.time()
    print(sln.gcdOfStrings(str1, str2))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase3 ...')
    str1 = "LEET"
    str2 = "CODE"
    tStart= time.time()
    print(sln.gcdOfStrings(str1, str2))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase4 ...')
    str1 = "LEETCODELEETCODELEETCODELEETCODELEETCODELEETCODELEETCODE"
    str2 = "LEETCODELEETCODELEETCODELEETCODE"
    tStart= time.time()
    print(sln.gcdOfStrings(str1, str2))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    