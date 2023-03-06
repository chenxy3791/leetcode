""" 
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""  
class MaxQueue:
""" 
执行结果：通过 显示详情
执行用时 :268 ms, 在所有 Python3 提交中击败了68.78%的用户
内存消耗 :17.1 MB, 在所有 Python3 提交中击败了100.00%的用户
 """
    def __init__(self):
        self.size = 0
        self.max  = -1
        self.q    = []

    def max_value(self) -> int:
        return self.max

    def push_back(self, value: int) -> None:
        self.q.append(value)
        self.size = self.size + 1
        if self.max < value:
            self.max = value

    def pop_front(self) -> int:
        if self.size == 0:
            return -1
        dat = self.q[0]
        self.q.pop(0)
        self.size = self.size - 1

        #update max if necessary
        if self.size == 0:
            self.max = -1
        elif self.max <= dat:
            self.max = self.q[0]
            for k in range(1,self.size):
                if self.max < self.q[k]:
                    self.max = self.q[k]
        return dat
        
# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == '__main__':    

    import time

    print('Testcase1...')    
    maxQ = MaxQueue()
    print(maxQ.push_back(1))
    print(maxQ.push_back(2))
    print(maxQ.max_value())
    print(maxQ.pop_front())
    print(maxQ.max_value())
    
    #["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value","pop_front","push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value","pop_front","max_value","push_back","push_back","max_value","push_back","max_value","max_value","max_value","push_back","pop_front","max_value","push_back","max_value","max_value","max_value","pop_front","push_back","push_back","push_back","push_back","pop_front","pop_front","max_value","pop_front","pop_front","max_value","push_back","push_back","pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front","max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back","pop_front"]
    #[[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]
    print('Testcase2...')    
    maxQ = MaxQueue()
    print(maxQ.max_value())
    print(maxQ.pop_front())
    print(maxQ.max_value())    
    print(maxQ.push_back(46))
    print(maxQ.max_value())
    print(maxQ.pop_front())
    print(maxQ.max_value())
    print(maxQ.pop_front())
    print(maxQ.push_back(868))
    print(maxQ.pop_front())    
