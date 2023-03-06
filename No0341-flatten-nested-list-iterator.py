"""
341. 扁平化嵌套列表迭代器
给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。

列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。

示例 1:

输入: [[1,1],2,[1,1]]
输出: [1,1,2,1,1]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
示例 2:

输入: [1,[4,[6]]]
输出: [1,4,6]
解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
    
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """

#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """

#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """

class NestedIterator:
    #def __init__(self, nestedList: [NestedInteger]):
    def __init__(self, nestedList):        
        print(type(nestedList))
        self.linear = []
        self.flattern(nestedList)

    def flattern(self, nlist) -> int:
        for item in nlist:            
            if item.isInteger():        
                self.linear.append(item.getInteger())
            else:            
                self.flattern(item.getList())
                
        # for items in nlist: 
        # #for k in range(len(nestedList)):TypeError: 'NestedInteger' object has no len()
        # #items = nestedList[k]
        #     if type(items) == int:
        #         self.linear.append(items)
        #     else:
        #         subLinear = self.flattern(items)
        #         self.linear = self.linear + subLinear
    
    def next(self) -> int:
        if self.hasNext:
            return self.linear.pop(0)
        else:
            return None
    
    def hasNext(self) -> bool:
        return len(self.linear) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
    
if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')    
    nestedList = [[1,1],2,[1,1]]
    i, v = NestedIterator(nestedList), []
    while i.hasNext(): 
        v.append(i.next())    
        
    print(v)
    
    # Testcase1
    