# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:35:08 2022

@author: Dell
"""

from typing import List
from collections import defaultdict
# from itertools import pairwise # Introduced in python 3.10

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # 首先，遍历words构建有向图并统计各节点的入度
        g = defaultdict(list)
        inDeg = {c: 0 for c in words[0]}
        #for s, t in pairwise(words):
        for k in range(len(words)-1):
            s,t = words[k], words[k+1] 
            for c in t:
                inDeg.setdefault(c, 0)
            for u, v in zip(s, t):
                if u != v:
                    # u不等于v则表明u的字典序一定在v之前，建立一条u->v的有向边，且v的入度数加一
                    g[u].append(v)
                    inDeg[v] += 1
                    break
            else:
                # 如果发现排在后面的单词是前面的单词的前缀则肯定违反字典序，直接返回空列表
                if len(s) > len(t):
                    return ""
        
        # 基于有向图进行广度优先搜索
        # 将入度为0的节点加入队列，这里用简单的列表来实现队列，是因为节点个数有限，不需要考虑存储开销
        # 一般情况下推荐使用collections.deque
        q = [u for u, d in inDeg.items() if d == 0]
        for u in q:
            # 顺序遍历u，模拟逐个从队列头部中取出各节点并移除的操作
            for v in g[u]:
                # 遍历u的各邻节点，由于u被移除，所以v的入度相应减一。
                # 如果减一后v的入度也变为0了就将v也加入队列（添加到表的尾部）
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
        return ''.join(q) if len(q) == len(inDeg) else ""

if __name__ == "__main__":
    
    sln = Solution()    
    words = ["wrt","wrf","er","ett","rftt"]
    print(sln.alienOrder(words))
    
    words = ["z","x"]
    print(sln.alienOrder(words))
    
    words = ["z","x","z"]
    print(sln.alienOrder(words))