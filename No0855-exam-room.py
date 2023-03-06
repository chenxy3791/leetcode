# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 07:39:21 2021

@author: chenxy

855. 考场就座
在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。

示例：

输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
 
提示：

1 <= N <= 10^9
在所有的测试样例中 ExamRoom.seat() 和 ExamRoom.leave() 最多被调用 10^4 次。
保证在调用 ExamRoom.leave(p) 时有学生正坐在座位 p 上。

2021-04-09:
    The first delivery, two slow.

"""

class ExamRoom:

    def __init__(self, N: int):
        self.occupancy = N*[0]        
        self.N = N

    def status(self) -> int:
        print('status(): Current occupied status: ', self.occupancy)
        
    def seat(self) -> int:
        # print('seat(): Current occupied status:', self.occupancy)
        if sum(self.occupancy) == 0:
            # print('No seat occupied')
            self.occupancy[0] = 1
            # print(self.occupancy)
            return 0
        
        lend = -1
        rend = -1
        maxintv = -1
        maxl = 0
        maxr = 0
        for k in range(self.N):
            if self.occupancy[k] == 1:
                lend = rend
                rend = k
                if lend == -1:
                    intv = 2*rend
                    lend = -rend
                else:
                    intv = 2*((rend - lend)//2)
                    
                if intv > maxintv:
                    maxintv = intv
                    maxl = rend
                    maxr = lend
        
        if self.occupancy[self.N-1] == 0:
            # print('(N-1) is unoccupied, and rend = ', rend)
            intv = 2*(self.N-1-rend)
            if intv > maxintv:
                maxintv = intv
                maxl = rend
                maxr = 2*(self.N-1) - rend
        rslt = (maxl + maxr)//2
        self.occupancy[rslt] = 1
        
        return rslt

    def leave(self, p: int) -> None:
        self.occupancy[p] = 0
        return
        
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

if __name__ == '__main__':        
    import time
    import random
        
    sln = ExamRoom(10)
    
    print(sln.seat())            
    sln.status()
    print(sln.seat())            
    sln.status()
    print(sln.seat())            
    print(sln.seat())                
    sln.leave(4)
    sln.status()
    print(sln.seat())            
    sln.status()

    sln = ExamRoom(1)
    
    print(sln.seat())            
    sln.status()
    sln.leave(0)
    sln.status()
    print(sln.seat())            
    sln.status()