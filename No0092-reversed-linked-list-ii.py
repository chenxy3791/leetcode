"""
92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

2021-03-19
执行用时：40 ms, 在所有 Python3 提交中击败了63.40%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了52.41%的用户

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# import sys
# sys.path.append(r'F:\CODEHUB\LEETCODE\utilfunc\')
# import ListNode as lnode
# from ListNode import ListNode
# chenxy@2021-03-19: How to use import in python?

def append_ListNode(val, head):    
    assert(head is not None)
    curNode = head
    while curNode.next is not None:
        curNode = curNode.next    
    curNode.next = ListNode(val, None)  

def print_list(head):
    assert(head is not None)    
    print("Singly linked list: ", end='')                                                
    current_ListNode = head                                                        
    print("head -->", end='')                                                          
    while(current_ListNode is not None):                                            
        print(current_ListNode.val, "-->", end='')                                         
        current_ListNode = current_ListNode.next                                       
    print("End")                  

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #print(left, right)
        if left == right:
            # Nothing to do
            return head

        if left == 1:
            leftNode = head
        else:
            cur = head
            # First, record the leftNode and the node before leftNode
            for _ in range(left-2): # Note, left and right are 1-indexed counting value
                cur = cur.next
            leftm1Node = cur
            leftNode   = cur.next
            # print(leftm1Node.val, leftNode.val)            

        nxt = leftNode.next
        cur = leftNode
        cnt = left
        while (cnt < right):
            prev = cur
            cur  = nxt
            nxt  = nxt.next
            cur.next = prev
            cnt = cnt + 1
        # After the above while-loop, cur should be the #(right) Node
        if left == 1:
            head = cur
        else:
            leftm1Node.next = cur
        leftNode.next   = nxt

        return head

if __name__ == '__main__':        
    #import time
    sln = Solution()
    
    # Generate one linked list
    head = ListNode(1)
    append_ListNode(2, head)                                                            
    append_ListNode(3, head)                                                            
    append_ListNode(4, head)                                                            
    append_ListNode(5, head)

    print('\nTestcase 1: ')    
    print('The original linked list is: ')
    print_list(head)                     
    head = sln.reverseBetween(head, 2, 4)
    print('After the reverse operation: ')
    print_list(head)                     

    print('\nTestcase 2: ')
    print('The original linked list is: ')
    print_list(head)                     
    head = sln.reverseBetween(head, 2, 4)
    print('After the reverse operation: ')
    print_list(head)                         

    print('\nTestcase 3: ')
    print('The original linked list is: ')
    print_list(head)                     
    head = sln.reverseBetween(head, 4, 5)
    print('After the reverse operation: ')
    print_list(head)                         

    print('\nTestcase 4: ')
    print('The original linked list is: ')
    print_list(head)                     
    head = sln.reverseBetween(head, 1, 3)
    print('After the reverse operation: ')
    print_list(head)                             