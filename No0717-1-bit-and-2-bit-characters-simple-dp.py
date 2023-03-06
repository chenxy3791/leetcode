# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 12:53:08 2022

@author: chenxy

717. 1比特与2比特字符

有两种特殊字符：
第一种字符可以用一个比特 0 来表示
第二种字符可以用两个比特(10 或 11)来表示、
给定一个以 0 结尾的二进制数组 bits ，如果最后一个字符必须是一位字符，则返回 true 。

示例 1:
输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。
示例 2:

输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。
所以最后一个字符不是一比特字符。

提示:
1 <= bits.length <= 1000
bits[i] == 0 or 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
"""
from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:        
        def dp(arr) -> bool:
            # baseline case
            if arr == [1,0] or arr == [1,1]:
                return False
            elif arr == [0]:
                return True
            elif arr == [1]:
                return False
            
            if arr[0] == 0:
                return dp(arr[1:])
            elif arr[0:2] == [1,1] or arr[0:2] == [1,0]:
                return dp(arr[2:])
            else:
                return False
        
        return dp(bits)

if __name__ == '__main__':        
    
    sln = Solution()

    bits = [1, 0, 0]
    print(sln.isOneBitCharacter(bits))

    bits = [1, 1, 1, 0]
    print(sln.isOneBitCharacter(bits))                
    
    bits = [1, 0, 1, 0, 1, 0, 1]
    print(sln.isOneBitCharacter(bits))                    