"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

思路：
可以使用双指针法.
在一个环形跑道上，A的速度为单位1，B的速度为单位2，那么两者从跑道的任意地方同向同时开跑，
那么总有两者相遇的时候（暂时不考虑起始位置一样），所以设置slow指针和fast指针来解决这个问题。
如果不存在环路，就会检测到链表的尾巴(tail.next == None)
    
"""
import math
from SinglyLinkedList import *

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False

        slowPtr = head
        fastPtr = head.next # Different starting-point for the convenience of while-loop

        while (1):            
            if fastPtr == slowPtr:
                return True
            elif slowPtr.next == None or fastPtr.next == None:
                return False
            elif fastPtr.next.next == None:
                return False
            else:
                slowPtr = slowPtr.next
                fastPtr = fastPtr.next.next

        return False

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    l1 = sllCycleCreation([3,2,0,4],1)    
    #SinglyLinkedList.printSll(l1)    
    print(sln.hasCycle(l1))

    print('Testcase2...')
    l1 = sllCycleCreation([1,2],0)    
    #SinglyLinkedList.printSll(l1)    
    print(sln.hasCycle(l1))

    print('Testcase3...')
    l1 = sllCycleCreation([1],-1)    
    #SinglyLinkedList.printSll(l1)    
    print(sln.hasCycle(l1))

    print('Testcase4...')
    l1 = sllCycleCreation([1,2,3,4,5],-1)    
    #SinglyLinkedList.printSll(l1)    
    print(sln.hasCycle(l1))