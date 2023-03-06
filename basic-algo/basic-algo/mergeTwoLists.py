"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
    
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def singlyLinkedListCreation(lin):
    if len(lin) == 0:
        return None
    ll_head  = ListNode(lin[0]) 
    prevNode = ll_head
    for k in range(1,len(lin)):
        #print('singlyLinkedListCreation: lin[{0}] = {1}'.format(k,lin[k]))
        prevNode.next = ListNode(lin[k])
        prevNode      = prevNode.next
    return ll_head

def printSingleLinkedList(ll_head):
    lout   = []
    curPtr = ll_head
    while curPtr != None:
        lout.append(curPtr.val)
        curPtr = curPtr.next
    print('printSingleLinkedList: ', lout)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Ptr = l1
        l2Ptr = l2
        head  = ListNode(0)
        prevNode = head
        while (l1Ptr != None) and (l2Ptr != None):
            if l1Ptr.val <= l2Ptr.val:
                prevNode.next = ListNode(l1Ptr.val)
                prevNode      = prevNode.next
                l1Ptr         = l1Ptr.next
            else:
                prevNode.next = ListNode(l2Ptr.val)                
                prevNode      = prevNode.next
                l2Ptr         = l2Ptr.next

        while l1Ptr != None:
            prevNode.next = ListNode(l1Ptr.val)
            prevNode      = prevNode.next
            l1Ptr         = l1Ptr.next

        while l2Ptr != None:
            prevNode.next = ListNode(l2Ptr.val)
            prevNode      = prevNode.next
            l2Ptr         = l2Ptr.next

        return head.next # Throw the first dummy node, which just serves as placeholder only.

if __name__ == '__main__':    

    sln   = Solution()

    print("Test of singlyLinkedListCreation and printSingleLinkedList...")
    l1 = singlyLinkedListCreation([1,2,4])
    print("l1 = ")
    printSingleLinkedList(l1)    

    # Testcase1
    print('\nTestcase1...')    
    l1 = singlyLinkedListCreation([1,2,4])
    l2 = singlyLinkedListCreation([1,3,4])

    print("l1 = ")
    printSingleLinkedList(l1)
    print("l2 = ")
    printSingleLinkedList(l2)
    
    newLL = sln.mergeTwoLists(l1,l2)
    print("The merged linked list is ")
    printSingleLinkedList(newLL)

    # Testcase2
    print('\nTestcase2...')    
    l1 = singlyLinkedListCreation([1,2,4])
    l2 = singlyLinkedListCreation([4,5,6])

    print("l1 = ")
    printSingleLinkedList(l1)
    print("l2 = ")
    printSingleLinkedList(l2)
    
    newLL = sln.mergeTwoLists(l1,l2)
    print("The merged linked list is ")
    printSingleLinkedList(newLL)

    # Testcase3
    print('\nTestcase3...')    
    l1 = singlyLinkedListCreation([])
    l2 = singlyLinkedListCreation([4,5,6])

    print("l1 = ")
    printSingleLinkedList(l1)
    print("l2 = ")
    printSingleLinkedList(l2)
    
    newLL = sln.mergeTwoLists(l1,l2)
    print("The merged linked list is ")
    printSingleLinkedList(newLL)