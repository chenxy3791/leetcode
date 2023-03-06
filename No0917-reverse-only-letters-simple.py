# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 07:31:17 2022

@author: chenxy

给你一个字符串 s ，根据下述规则反转字符串：

所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。
返回反转后的 s 。
 
示例 1：
输入：s = "ab-cd"
输出："dc-ba"

示例 2：
输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

示例 3：
输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
 
提示:
1 <= s.length <= 100
s 仅由 ASCII 值在范围 [33, 122] 的字符组成
s 不含 '\"' 或 '\\'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-only-letters
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        slst = list(s)
        left_to_right = 0
        right_to_left = len(slst)-1
        while right_to_left > left_to_right:
            if not slst[left_to_right].isalpha():
                left_to_right += 1
                continue
            if not slst[right_to_left].isalpha():
                right_to_left -= 1
                continue
            
            # Both are English letters, swap them
            slst[left_to_right],slst[right_to_left] = slst[right_to_left],slst[left_to_right]
            left_to_right += 1
            right_to_left -= 1
        
        return ''.join(slst)

if __name__ == '__main__':        
    
    sln = Solution()    
    
    s = "ab-cd"
    print('s = {0}: {1}'.format(s,sln.reverseOnlyLetters(s)))
    
    s = "a-bC-dEf-ghIj"
    print('s = {0}: {1}'.format(s,sln.reverseOnlyLetters(s)))
    
    s = "Test1ng-Leet=code-Q!"
    print('s = {0}: {1}'.format(s,sln.reverseOnlyLetters(s)))
    
    s = ''
    print('s = {0}: {1}'.format(s,sln.reverseOnlyLetters(s)))
    
    