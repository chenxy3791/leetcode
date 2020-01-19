"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
    
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:             
        assert(n > 0)
        lLen = 0
        curPtr = head
        while curPtr != None:
            lLen = lLen + 1
            curPtr = curPtr.next

        if lLen == n: # To delete the head node
            head = head.next
            return head

        m = lLen - n         
        #print('lLen = {0}, n = {1}, m = {2}'.format(lLen,n,m))
        curPtr = head       
        for _ in range(m-1):
            curPtr = curPtr.next            
        curPtr.next = curPtr.next.next

        return head

if __name__ == '__main__':    

    sln   = Solution()

    # Testcase1
    print('\nTestcase1...')    
    l = [1,2,3,4,5]
    ll_head = ListNode(l[0]) 
    prevPtr  = ll_head
    for k in range(1,len(l)):
        prevPtr.next = ListNode(l[k])
        prevPtr      = prevPtr.next

    print("The original linked list is : ")
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next

    n = 2
    ll_head = sln.removeNthFromEnd(ll_head,n)
    print("After the {0}-th node to the end being deleted, the linked list becomes : ".format(n))
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next

    # Testcase2
    print('\nTestcase2...')    
    l = [1,2,3,4,5]
    ll_head = ListNode(l[0]) 
    prevPtr  = ll_head
    for k in range(1,len(l)):
        prevPtr.next = ListNode(l[k])
        prevPtr      = prevPtr.next

    print("The original linked list is : ")
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next

    n = 1
    ll_head = sln.removeNthFromEnd(ll_head,n)
    print("After the {0}-th node to the end being deleted, the linked list becomes : ".format(n))
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next

    # Testcase3
    print('\nTestcase3...')    
    l = [1,2,3,4,5]
    ll_head = ListNode(l[0]) 
    prevPtr  = ll_head
    for k in range(1,len(l)):
        prevPtr.next = ListNode(l[k])
        prevPtr      = prevPtr.next

    print("The original linked list is : ")
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next

    n = 5
    ll_head = sln.removeNthFromEnd(ll_head,n)
    print("After the {0}-th node to the end being deleted, the linked list becomes : ".format(n))
    curPtr = ll_head
    while curPtr != None:
        print(curPtr.val)
        curPtr = curPtr.next