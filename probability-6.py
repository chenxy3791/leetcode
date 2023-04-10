# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:48:25 2022

@author: Dell
"""

import numpy as np
import bisect

class Game:
    def __init__(self, transfer, cost):
        self.n = transfer.shape[0]
        self.cost = cost
        self.transfer = transfer
        for i in range(self.n):
            for j in range(1, self.transfer.shape[1]):
                self.transfer[i][j] += self.transfer[i][j - 1]

    def step(self, pos):
        return bisect.bisect_left(self.transfer[pos]
                                 ,np.random.rand())

    def __call__(self):
        pos = 0
        pay = 0
        while pos != self.n:
            pay += self.cost[pos]
            pos = self.step(pos)
        pay += self.cost[self.n]
        return pay

transfer = np.array([[0.1, 0.9, 0.0, 0.0, 0.0]
                    ,[0.3, 0.0, 0.7, 0.0, 0.0]
                    ,[0.0, 0.4, 0.0, 0.6, 0.0]
                    ,[0.0, 0.0, 0.5, 0.0, 0.5]
                    ])
cost = np.array([0.0, 1.0, 2.0, 3.0, -10.0])
game = Game(transfer, cost)

def test():
    T = int(1e5)
    total_pay = 0
    for t in range(T):
        total_pay += game()
    print("Average income: {:.4f}".format(total_pay / T))

for i in range(10):
    test()

# 作者：FennelDumplings
# 链接：https://leetcode-cn.com/leetbook/read/probability-problems/ney8cv/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。