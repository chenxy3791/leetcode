# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 07:59:53 2022

@author: chenxy

838. 推多米诺
n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。
每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。
就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。
给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：

dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
返回表示最终状态的字符串。
补充说明: 最终状态的字符串仍以'L','R','.'表示，分别表示倒向左边、导向右边及保持垂直竖立。

示例 1：
输入：dominoes = "RR.L"
输出："RR.L"
解释：第一张多米诺骨牌没有给第二张施加额外的力。

示例 2：
输入：dominoes = ".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
 
提示：
n == dominoes.length
1 <= n <= 10^5
dominoes[i] 为 'L'、'R' 或 '.'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/push-dominoes
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d_list = list(dominoes)
        print(d_list)
        begin = tuple(('L', -1))
        end   = None

        def finalState(begin,end):
            print('finalState: ',begin,end)
            if end[0] == begin[0]:
                for k in range(begin[1]+1,end[1]):
                    d_list[k] = begin[0]
            elif begin[0] == 'R' and end[0] == 'L':
                for k in range(begin[1]+1,end[1]):
                    if (k-begin[1]) < (end[1]-k):
                        d_list[k] = 'R'
                    elif (k-begin[1]) > (end[1]-k):
                        d_list[k] = 'L'
                    # else: keep unchanged.                            
            # else: keep unchanged.            
        
        for k in range(len(d_list)):
            if d_list[k] != '.':
                print(k,d_list)
                end = tuple((d_list[k], k))
                # Decide the final state of the segment between the current begin and end
                finalState(begin,end)
                begin = end
        if begin[1] < len(d_list) - 1:
            end = ('R', len(d_list))
            finalState(begin,end)

        return ''.join(d_list)            
            
if __name__ == '__main__':        
    
    sln = Solution()

    dominoes = "RR.L"
    print(sln.pushDominoes(dominoes))                 
                
    dominoes = ".L.R...LR..L.."
    print(sln.pushDominoes(dominoes))                 

    dominoes = "...L"
    print(sln.pushDominoes(dominoes))                                     