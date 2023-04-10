# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 07:34:05 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     def diff_is_one(s1,s2)->bool:
    #         cnt=0
    #         for k in range(len(s1)):
    #             if s1[k]!=s2[k]:
    #                 cnt+=1
    #         return cnt==1
        
    #     # Construct adjacency list first
    #     endIdx  = -1
    #     wordList.insert(0, beginWord)
    #     for k,word in enumerate(wordList):
    #         if endWord==word:
    #             endIdx = k
    #     if endIdx<0:
    #         return 0
        
    #     adjlist = [ [] for k in range(len(wordList)) ]
    #     for k in range(len(wordList)):
    #         for j in range(k,len(wordList)):
    #             if diff_is_one(wordList[k], wordList[j]):
    #                 adjlist[k].append(j)
    #                 adjlist[j].append(k)
                    
    #     # print(bank,adjlist)
    #     q = deque([(0,0)])
    #     visited = set([0])
    #     while len(q)>0:
    #         node,layer = q.popleft()
    #         if node == endIdx:
    #             return layer+1
    #         for nxt in adjlist[node]:
    #             if nxt not in visited:
    #                 q.append((nxt,layer+1))
    #                 visited.add(nxt)
    #     return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_is_one(s1,s2)->bool:
            cnt=0
            for k in range(len(s1)):
                if s1[k]!=s2[k]:
                    cnt+=1
            return cnt==1
        
        # Construct adjacency list first
        endIdx  = -1
        wordList.insert(0, beginWord)
        for k,word in enumerate(wordList):
            if endWord==word:
                endIdx = k
        if endIdx<0:
            return 0
        
        adjlist = [ [] for k in range(len(wordList)) ]
        for k in range(len(wordList)):
            for j in range(k,len(wordList)):
                if diff_is_one(wordList[k], wordList[j]):
                    adjlist[k].append(j)
                    adjlist[j].append(k)
                    
        # print(bank,adjlist)
        q1 = deque([(0,0)])
        visited1 = dict()
        visited1[0] = 0
        q2 = deque([(endIdx,0)])
        visited2 = dict()
        visited2[endIdx] = 0
        while len(q1)>0 or len(q2)>0:
            if len(q1)>0:
                node1,layer1 = q1.popleft()
                if node1 in visited2:
                    return layer1+visited2[node1]+1
                for nxt in adjlist[node1]:
                    if nxt not in visited1:
                        q1.append((nxt,layer1+1))
                        visited1[nxt]=layer1+1

            if len(q2)>0:            
                node2,layer2 = q2.popleft()
                if node2 in visited1:
                    return layer2+visited1[node2]+1
                for nxt in adjlist[node2]:
                    if nxt not in visited2:
                        q2.append((nxt,layer2+1))
                        visited2[nxt]=layer2+1
                    
        return 0
    
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         def addWord(word: str):
#             if word not in wordId:
#                 nonlocal nodeNum
#                 wordId[word] = nodeNum
#                 nodeNum += 1
        
#         def addEdge(word: str):
#             addWord(word)
#             id1 = wordId[word]
#             chars = list(word)
#             for i in range(len(chars)):
#                 tmp = chars[i]
#                 chars[i] = "*"
#                 newWord = "".join(chars)
#                 addWord(newWord)
#                 id2 = wordId[newWord]
#                 edge[id1].append(id2)
#                 edge[id2].append(id1)
#                 chars[i] = tmp

#         wordId = dict()
#         edge = collections.defaultdict(list)
#         nodeNum = 0

#         for word in wordList:
#             addEdge(word)
        
#         addEdge(beginWord)
#         if endWord not in wordId:
#             return 0
        
#         disBegin = [float("inf")] * nodeNum
#         beginId = wordId[beginWord]
#         disBegin[beginId] = 0
#         queBegin = collections.deque([beginId])

#         disEnd = [float("inf")] * nodeNum
#         endId = wordId[endWord]
#         disEnd[endId] = 0
#         queEnd = collections.deque([endId])

#         while queBegin or queEnd:
#             queBeginSize = len(queBegin)
#             for _ in range(queBeginSize):
#                 nodeBegin = queBegin.popleft()
#                 if disEnd[nodeBegin] != float("inf"):
#                     return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
#                 for it in edge[nodeBegin]:
#                     if disBegin[it] == float("inf"):
#                         disBegin[it] = disBegin[nodeBegin] + 1
#                         queBegin.append(it)

#             queEndSize = len(queEnd)
#             for _ in range(queEndSize):
#                 nodeEnd = queEnd.popleft()
#                 if disBegin[nodeEnd] != float("inf"):
#                     return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
#                 for it in edge[nodeEnd]:
#                     if disEnd[it] == float("inf"):
#                         disEnd[it] = disEnd[nodeEnd] + 1
#                         queEnd.append(it)
        
#         return 0


if __name__ == "__main__":
    
    sln = Solution()
    
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(sln.ladderLength(beginWord, endWord, wordList))
        
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]  
    print(sln.ladderLength(beginWord, endWord, wordList))

    with open('No0127-testcase.py','r') as f:
        exec(f.read())  
    tstart=time.time()    
    print(sln.ladderLength(beginWord, endWord, wordList))
    tstop=time.time()
    print('tcost = {0:4.2f}(sec)'.format(tstop-tstart))    
    