# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 17:10:55 2022

@author: Dell
"""

class Solution:
    def maximumSubsequenceCount1(self, text: str, pattern: str) -> int:
        def countSubSeq(t):
            p0_cnt     = 0
            subseq_cnt = 0
            for k in range(len(t)):
                if t[k] == pattern[0]:
                    p0_cnt += 1
                elif t[k] == pattern[1]:
                    subseq_cnt += p0_cnt
            return subseq_cnt
        subseq_max = 0
        for k in range(len(text)+1):
            t_tmp = text[:k] + pattern[0] + text[k:]
            subseq_cnt = countSubSeq(t_tmp)
            # print(t_tmp,subseq_cnt)
            subseq_max = subseq_cnt if subseq_max<subseq_cnt else subseq_max

            t_tmp = text[:k] + pattern[1] + text[k:]
            subseq_cnt = countSubSeq(t_tmp)
            # print(t_tmp,subseq_cnt)
            subseq_max = subseq_cnt if subseq_max<subseq_cnt else subseq_max            
        return subseq_max

    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        def countSubSeq(t):
            p0_cnt     = 0
            subseq_cnt = 0
            for k in range(len(t)):
                if t[k] == pattern[0]:
                    p0_cnt += 1
                if t[k] == pattern[1]:
                    subseq_cnt += p0_cnt
            if pattern[0] == pattern[1]:
                subseq_cnt = p0_cnt * (p0_cnt - 1) // 2
            return subseq_cnt

        subseq_cnt0 = countSubSeq(pattern[0] + text)
        subseq_cnt1 = countSubSeq(text + pattern[1])

        return subseq_cnt0 if subseq_cnt0>=subseq_cnt1 else subseq_cnt1            
    
if __name__ == '__main__':
    
    sln = Solution()
    
    text = "abdcdbc"
    pattern = "ac"
    print(sln.maximumSubsequenceCount(text, pattern))
    
    text = "aabb"
    pattern = "ab"
    print(sln.maximumSubsequenceCount(text, pattern))
    
    text = "mffiqmrvjmkfmbnaivajzecfdta"
    pattern = "hh"
    print(sln.maximumSubsequenceCount(text, pattern))
    
    text = "fwymvreuftzgrcrxczjacqovduqaiig"
    pattern = "yy"    
    print(sln.maximumSubsequenceCount(text, pattern))    