"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
    
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print(node, node.val, node.next)
        nodeTmp = node
        while 1:
            nodeTmp.val = nodeTmp.next.val
            if nodeTmp.next.next == None:                
                nodeTmp.next = None
                break
            else:
                nodeTmp = nodeTmp.next                
            
if __name__ == '__main__':    

    sln   = Solution()

    head = [4,5,1,9]
    lNode0 = ListNode(4)
    lNode1 = ListNode(5)
    lNode2 = ListNode(1)
    lNode3 = ListNode(9)
    lNode0.next = lNode1;
    lNode1.next = lNode2;
    lNode2.next = lNode3;

    # Testcase0
    print('Testcase0...')    
    sln.deleteNode(lNode2)
    print("After node deleting, the linked list becomes : ")
    print(lNode0.val, lNode0.next.val, lNode0.next.next.val)

    