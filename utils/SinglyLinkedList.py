# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://codingpointer.com/python-tutorial/singly-linked-list#:~:text=Singly%20linked%20list%20python%20program%20Linked%20list%20is,linked%20list%20contains%20two%20fields%20in%20each%20ListNode.
# Global variable for header and tail pointer in singly linked list.                                                                         
# chenxy@2021-03-19: 
# In the original implementation, 'tail' is provided as a-priori-known parameter.
# Usually, tail is not provided in singly linked list. But a-priori-known tail will improve the operation efficiency. 
# However, it may hurt the universality. Here, I removed it.
# Also in the original implementation, 'head' and 'tail' are treated as global variable.
# I don't think it is a reasonable choice.
# Here, I changed to pass head as function parameter.

def create_SinglyLinkedList(valList):    
    head = ListNode(valList[0])
    for k in range(1, len(valList)):
        append_ListNode(valList[k], head)                                                            
    return head
    
# appends new ListNode at the end in singly linked list. 
# If 'head' is None, the linked list will be created.
def append_ListNode(val, head):        
    if head != None:
        curNode = head
        while curNode.next is not None:
            curNode = curNode.next    
        curNode.next = ListNode(val, None)                                                     
    else:
        head = ListNode(val, None)

# inserts new ListNode at specific position in singly linked list.
def insert_ListNode(val, position, head):
    assert(head is not None)    
    current_ListNode = head                                                        
    while(position > 1):                                                        
        position -= 1                                                          
        current_ListNode = current_ListNode.next                                       
    temp_next = current_ListNode.next                                              
    lstNode = ListNode(val, temp_next)                                                
    current_ListNode.next = lstNode                                                               
            
# prints singly linked list values.                                                                    
def print_linkedlist(head):
    assert(head is not None)    
    print("Single linked list: ", end='')                                                
    current_ListNode = head                                                        
    print("head -->", end='')                                                          
    while(current_ListNode is not None):                                            
        print(current_ListNode.val, "-->", end='')                                         
        current_ListNode = current_ListNode.next                                       
    print("End")                  
                                              
# removes matching first ListNode for particular value in linked list.                                                                              
def remove_ListNode(val, head): 
    assert(head is not None)                                                                  
    current_ListNode = head
    previous_ListNode = None                                                       
    while(current_ListNode is not None):                                            
        if current_ListNode.val == val:                                             
            if previous_ListNode is not None:                                       
                previous_ListNode.next = current_ListNode.next                         
            else:                                                               
                head = current_ListNode.next                                       
        previous_ListNode = current_ListNode                                           
        current_ListNode = current_ListNode.next                                       
                            
# reverses singly linked list values.                                                    
def reverse_linked_list(head):  
    assert(head is not None)                                                                                                                   
    current_ListNode = head                                                        
    previous_ListNode = None                                                       
    while(current_ListNode is not None):                                            
        next_ListNode = current_ListNode.next                                          
        current_ListNode.next = previous_ListNode                                      
        previous_ListNode = current_ListNode                                           
        current_ListNode = next_ListNode                                               
        head = previous_ListNode
    return head  

# getting ListNodes count in singly linked list.
def count(head):                                                                    
    assert(head is not None)                                                                                                                   
    current_ListNode = head                                                        
    counter = 0                                                                
    while(current_ListNode is not None):                                            
        counter += 1                                                           
        current_ListNode = current_ListNode.next                                       
    print("Single linked list ListNode count:", counter)                                                  
                                                                                
if __name__ == "__main__":                                      

    head = create_SinglyLinkedList([20,13,24,56])                
    
    # head = ListNode(20)
    # append_ListNode(13, head)                                                            
    # append_ListNode(24, head)                                                            
    # append_ListNode(56, head)                                                            
    print_linkedlist(head)                                                               
    insert_ListNode(45, 2, head)                                                         
    print("After insert ListNode at 2")                                             
    print_linkedlist(head)                                                               
    remove_ListNode(13, head)                                                            
    print("After removal of ListNode 13")                                           
    print_linkedlist(head)                                                               
    head = reverse_linked_list(head)                                                      
    print("After reversing singly linked list")                                 
    print_linkedlist(head)  
    count(head)       
