# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 08:17:01 2022

@author: chenxy
432. 全 O(1) 的数据结构
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 AllOne 类：

AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。

示例：
输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
 

提示：
1 <= key.length <= 10
key 由小写英文字母组成
测试用例保证：在每次调用 dec 时，数据结构中总存在 key
最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-oone-data-structure
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class AllOne:
    
#     def __init__(self):
#         self.strCnt = dict()

#     def inc(self, key: str) -> None:
#         if key in self.strCnt:
#             self.strCnt[key] = self.strCnt[key] + 1
#         else:
#             self.strCnt[key] = 1

#     def dec(self, key: str) -> None:
#         self.strCnt[key] = self.strCnt[key] - 1
#         if self.strCnt[key] == 0:
#             # remove this key
#             self.strCnt.pop(key)

#     def getMaxKey(self) -> str:
#         maxValue = 0
#         maxKey   = ''
#         for key in self.strCnt:
#             if maxValue < self.strCnt[key]:
#                 maxValue = self.strCnt[key]
#                 maxKey = key
#         return maxKey        

#     def getMinKey(self) -> str:
#         minValue = float('inf')
#         minKey   = ''
#         for key in self.strCnt:
#             if minValue > self.strCnt[key]:
#                 minValue = self.strCnt[key]
#                 minKey = key
#         return minKey 

#     def print(self):
#         for key in self.strCnt:
#             print(key, self.strCnt[key])

class AllOne:
    
    def __init__(self):
        self.strCnt   = dict()
        self.maxValue = 0
        self.minValue = float('inf')
        self.maxKey   = ''
        self.minKey   = ''

    def searchMinKey(self):
        self.minValue = float('inf')
        self.minKey   = ''
        for key in self.strCnt:
            if self.minValue > self.strCnt[key]:
                self.minValue = self.strCnt[key]
                self.minKey = key                        

    def searchMaxKey(self):
        self.maxValue = 0
        self.maxKey   = ''
        for key in self.strCnt:
            if self.maxValue < self.strCnt[key]:
                self.maxValue = self.strCnt[key]
                self.maxKey = key
        
    def inc(self, key: str) -> None:
        if key in self.strCnt:
            # Existing key increment.
            self.strCnt[key] = self.strCnt[key] + 1
            if len(self.strCnt) == 1:
                self.minValue = self.maxValue = self.strCnt[key]
                self.minKey   = self.maxKey   = key        
            else:
                # Incremental update of maxKey
                if self.maxValue < self.strCnt[key]:
                    self.maxValue = self.strCnt[key]
                    self.maxKey = key         

                # If this key is the original minKey, search for the new minKey                    
                if self.minKey == key:
                    self.searchMinKey()                                            
        else:
            # New key added.
            self.strCnt[key] = 1            
            # Always set the newly added item as the minKey
            self.minValue = 1
            self.minKey = key                                        
            
            if len(self.strCnt) == 1:
                self.maxValue = 1
                self.maxKey   = key        

    def dec(self, key: str) -> None:
        self.strCnt[key] = self.strCnt[key] - 1
        if self.strCnt[key] > 0:            
            if self.minValue > self.strCnt[key]:
                # Incremental update of minKey               
                self.minValue = self.strCnt[key]
                self.minKey = key                                       
            if key == self.maxKey:
                # If it is the original maxKey, search for the maxKey again
                self.searchMaxKey()                        
        else:
            # remove this key
            self.strCnt.pop(key)
        
            if len(self.strCnt)==0:
                self.maxValue = 0
                self.minValue = float('inf')
                self.maxKey   = ''
                self.minKey   = ''        
            else:
                if key == self.minKey:
                    self.searchMinKey()
                if key == self.maxKey:
                    self.searchMaxKey()
                                    
    def getMaxKey(self) -> str:
        return self.maxKey        

    def getMinKey(self) -> str:
        return self.minKey 

    def print(self):
        print('The details:',end='')
        print('minKey={0}, minValue={1}, maxKey={2}, maxValue={3}'.format(self.minKey, self.minValue, self.maxKey, self.maxValue))
        # for key in self.strCnt:
            # print(key, self.strCnt[key])
        print(self.strCnt)


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

if __name__ == '__main__':            
    
    print('testcase 1....')
    allOne = AllOne()
    cmd = ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
    para = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    # expected output: [null, null, null, "hello", "hello", null, "hello", "leet"]
    for k in range(1,len(cmd)):
        print(cmd[k], para[k])
        if cmd[k] == 'inc':
            allOne.inc(para[k][0])
        elif cmd[k] == 'dec':
            allOne.dec(para[k][0])
        elif cmd[k] == 'getMaxKey':
            print(allOne.getMaxKey())
        elif cmd[k] == 'getMinKey':
            print(allOne.getMinKey())

        # allOne.print()    

    print('testcase 2....')
    allOne = AllOne()    
    cmd = ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
    para = [[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]    

    # expected output: [null,null,null,null,null,"hello",null,null,null,null,null,null,null,"leet"]
    for k in range(1,len(cmd)):
        print(cmd[k], para[k])
        if cmd[k] == 'inc':
            allOne.inc(para[k][0])
        elif cmd[k] == 'dec':
            allOne.dec(para[k][0])
        elif cmd[k] == 'getMaxKey':
            print(allOne.getMaxKey())
        elif cmd[k] == 'getMinKey':
            print(allOne.getMinKey())

        # allOne1.print()    

    print('testcase 3....')
    allOne = AllOne()
    cmd = ["AllOne","inc","inc","inc","dec","inc","inc","getMaxKey","dec","dec","dec","getMaxKey"]
    para = [[],["hello"],["world"],["hello"],["world"],["hello"],["leet"],[],["hello"],["hello"],["hello"],[]]
    # expected output: [null,null,null,null,null,null,null,"hello",null,null,null,"leet"]
    
    for k in range(1,len(cmd)):
        print(cmd[k], para[k])
        if cmd[k] == 'inc':
            allOne.inc(para[k][0])
        elif cmd[k] == 'dec':
            allOne.dec(para[k][0])
        elif cmd[k] == 'getMaxKey':
            print(allOne.getMaxKey())
        elif cmd[k] == 'getMinKey':
            print(allOne.getMinKey())
        allOne.print()                