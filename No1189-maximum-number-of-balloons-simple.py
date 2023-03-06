# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:08:56 2022

@author: chenxy

1189. “气球” 的最大数量
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
示例 1：
    输入：text = "nlaebolko"
    输出：1
示例 2：
    输入：text = "loonbalxballpoon"
    输出：2
示例 3：
    输入：text = "leetcode"
    输出：0

提示：
    1 <= text.length <= 10^4
    text 全部由小写英文字母组成
    
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import time
import random
from collections import Counter
    
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
# =============================================================================
#         执行用时：40 ms, 在所有 Python3 提交中击败了32.13%的用户
#         内存消耗：15.1 MB, 在所有 Python3 提交中击败了16.22%的用户        
# =============================================================================
        cnt_dict = dict()
        cnt_dict['b'] = 0
        cnt_dict['a'] = 0
        cnt_dict['l'] = 0
        cnt_dict['o'] = 0
        cnt_dict['n'] = 0
        
        for c in text:
            if c in ['b','a','l','o','n']:
                cnt_dict[c] = cnt_dict[c] + 1
        
        cnt_dict['l'] = cnt_dict['l'] // 2
        cnt_dict['o'] = cnt_dict['o'] // 2
        
        return min(cnt_dict.values())

    def maxNumberOfBalloons2(self, text: str) -> int:
# =============================================================================
# 执行用时：44 ms, 在所有 Python3 提交中击败了14.41%的用户
# 内存消耗：15.1 MB, 在所有 Python3 提交中击败了40.84%的用户        
# =============================================================================
        cnt = Counter(c for c in text if c in 'balon')
        cnt['l'] = cnt['l'] // 2
        cnt['o'] = cnt['o'] // 2
        
        return min(cnt.values()) if len(cnt)==5 else 0
        

if __name__ == '__main__':        
    
    sln = Solution()

    text = "nlaebolko"
    print(sln.maxNumberOfBalloons(text))            
    print(sln.maxNumberOfBalloons2(text))                
                    
    text = "loonbalxballpoon"
    print(sln.maxNumberOfBalloons(text))                 
    print(sln.maxNumberOfBalloons2(text))                       

    text = "leetcode"
    print(sln.maxNumberOfBalloons(text))                 
    print(sln.maxNumberOfBalloons2(text))                        

    # Random testcase    
    # fullCharSet = 'abcdefghijklmnopqrstuvwxyz'
    # thisSet     = 'ballon'
    