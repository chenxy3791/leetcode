""" 
876. 链表的中间结点
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 
提示：
给定链表的结点数介于 1 和 100 之间。

解题思路：
快慢指针。
块指针前进两步，慢指针前进一步

"""
import math
import time
import numpy as np

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
        if fast.next == None:
            return slow
        else:
            return slow.next
                           
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    [1,2,3,4,5]
    head   = ListNode(1)
    second = ListNode(2)
    third  = ListNode(3)
    fourth = ListNode(4)
    fifth  = ListNode(5)
    head.next = second
    second.next = third
    third.next  = fourth
    fourth.next = fifth
    tStart= time.time()
    middle = sln.middleNode(head)
    h = middle
    while h != None:
        print(h.val)
        h = h.next
    
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    [1,2,3,4,5,6]
    head   = ListNode(1)
    second = ListNode(2)
    third  = ListNode(3)
    fourth = ListNode(4)
    fifth  = ListNode(5)
    sixth  = ListNode(6)
    head.next   = second
    second.next = third
    third.next  = fourth
    fourth.next = fifth
    fifth.next  = sixth
    tStart= time.time()
    middle = sln.middleNode(head)
    h = middle
    while h != None:
        print(h.val)
        h = h.next
    
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    
    
    print('\ntestcase3 ...')
    [1]
    head   = ListNode(1)
    middle = sln.middleNode(head)
    h = middle
    while h != None:
        print(h.val)
        h = h.next
    
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    
