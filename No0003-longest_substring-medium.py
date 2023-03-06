# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:37:51 2018

3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
 
示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
     
提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
# from typing import List	
# import random
# from collections import defaultdict
# import time
# import numpy as np
# from math import sqrt
# from collections import deque
# import itertools as it
# import numpy as np
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        start  = 0
        curptr = 1
        maxlen = 1        
        while curptr < len(s):                        
            # print(start, curptr)
            if s[curptr] in s[start:curptr]:
                # print(s[start:curptr])
                curlen = curptr - start
                maxlen = curlen if maxlen < curlen else maxlen
                start  = s[start:curptr].index(s[curptr]) + start + 1
            curptr += 1
        # last character processing
        # print(start, curptr)
        curlen = curptr - start
        maxlen = curlen if maxlen < curlen else maxlen
        
        return maxlen
        
if __name__ == '__main__':            
    
    sln = Solution()

    s = "au"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))             

    s = "dvdf"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))             

    s = "ckilbkd"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))             
    
    s = "abcabcbb"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))             

    s = "bbbbb"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))           

    s = "pwwkew"
    tStart = time.time()        
    ans = sln.lengthOfLongestSubstring(s)
    tElapsed = time.time() - tStart            
    print('ans={0}, tCost={1:3.2f}(sec)'.format(ans,tElapsed))         
    
    