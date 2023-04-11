# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:12:30 2022

@author: Dell

ref1: https://www.codespeedy.com/topological-sorting-in-python/#:~:text=%20Algorithm%20for%20endpological%20Sorting%20%201%20Step,-2%20until%20the%20graph%20is%20empty.%20More%20
ref2: https://leetcode.cn/problems/Jf1JuT/solution/wai-xing-wen-zi-dian-by-leetcode-solutio-to66/
"""

from collections import defaultdict

class Graph:
    def __init__(self, isDirected=False):
        # 以邻接表的方式表示一张图
        self.graph = defaultdict(list)
        self.isDirected = isDirected

    def addEdge(self, start, end):
# =============================================================================
#       添加一条边
# =============================================================================
        
        # 将end添加到start节点的邻接表
        self.graph[start].append(end)

        if self.isDirected is False:
            # 如果是无向图，则双向追加。这个与拓扑排序无关，是作为一般的图构建方法放在这里的。
            self.graph[end].append(start)
        else:
            self.graph[end] = self.graph[end]

    def topoSortvisit0(self, s, visited, sortlist):
        visited[s] = True

        for i in self.graph[s]:
            if not visited[i]:
                self.topoSortvisit0(i, visited, sortlist)

        sortlist.insert(0, s)

    def topoSortDfs0(self):
        visited = {i: False for i in self.graph}

        sortlist = []
       
        for u in self.graph:
            if not visited[u]:
                self.topoSortvisit0(u, visited, sortlist)

        return sortlist

    def topoSortvisit1(self, s, visited, sortlist):
        visited[s] = 1 #将节点s的状态置为“访问中”

        succ = True
        for i in self.graph[s]:
            # 遍历节点s的邻接节点
            if 0 == visited[i]:
                succ = succ and self.topoSortvisit1(i, visited, sortlist)
            elif 1 == visited[i]:
                # 找到一个环路，不存在拓扑排序
                return False
        if succ:
            # 针对当前节点的所有邻接点的搜索都成功结束，意味着所有邻接点都已经加入拓扑排序列表
            # 将当前节点置为“已访问”并将它加入拓扑排序列表。
            visited[s] = 2 #将节点s的状态置为“已访问”
            sortlist.insert(0, s) # 注意是插入到表头
            return True
        else:
            return False

    def topoSortDfs1(self):
        
        # 所有节点状态初始化为“未访问”
        visited = {i: 0 for i in self.graph}

        sortlist = []
       
        for u in self.graph:
            # 最外层是对每个节点进行遍历，不会出现重复。
            # 中途检测到从任何一个节点出发拓扑排序失败（检测到环）的话，都算失败。
            if 0 == visited[u]:
                if not self.topoSortvisit1(u, visited, sortlist):
                    return None
        return sortlist

    def topoSortBfs(self):
        # 查询统计各节点的入度
        inDeg = {node:0 for node in self.graph}
        for node in self.graph:
            for adj in self.graph[node]:
                inDeg[adj] += 1

        # 用一个list来简单地模拟队列
        # 首先将所有入度为0的节点加入队列
        q = [node for node, d in inDeg.items() if d == 0]
        for u in q:
            # 顺序遍历u，模拟逐个从队列头部中取出各节点并移除的操作
            for v in self.graph[u]:
                # 遍历u的各邻节点，由于u被移除，所以v的入度相应减一。
                # 如果减一后v的入度也变为0了就将v也加入队列（添加到表的尾部）
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    q.append(v)
                    
        if len(q) < len(self.graph): return None
        return q
        
if __name__ == '__main__':
 
    g = Graph(isDirected=True)

    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 6)
    g.addEdge(4, 6)

    # Testcase1
    print("\nTestcase1 ... ")
    print("topological Sort:", g.topoSortDfs0())
    print("topological Sort:", g.topoSortDfs1())
    print("topological Sort:", g.topoSortBfs())
    
    # Testcase2
    print("\nTestcase2 ... ")
    g.addEdge(3, 2)
    print("topological Sort:", g.topoSortDfs0())
    print("topological Sort:", g.topoSortDfs1())
    print("topological Sort:", g.topoSortBfs())
    
    # Testcase3
    print("\nTestcase3 ... ")
    g.addEdge(4, 2)
    print("topological Sort:", g.topoSortDfs0())
    print("topological Sort:", g.topoSortDfs1())
    print("topological Sort:", g.topoSortBfs())
    