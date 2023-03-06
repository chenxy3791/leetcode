# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def sllCreation(lin):
    if len(lin) == 0:
        return None
    ll_head  = ListNode(lin[0]) 
    prevNode = ll_head
    for k in range(1,len(lin)):
        #print('singlyLinkedListCreation: lin[{0}] = {1}'.format(k,lin[k]))
        prevNode.next = ListNode(lin[k])
        prevNode      = prevNode.next
    return ll_head

def sllCycleCreation(lin, pos):
    if len(lin) == 0:
        return None
    ll_head  = ListNode(lin[0]) 
    prevNode = ll_head
    for k in range(1,len(lin)):
        #print('singlyLinkedListCreation: lin[{0}] = {1}'.format(k,lin[k]))
        prevNode.next = ListNode(lin[k])
        prevNode      = prevNode.next
    # NOW, prevNode points to the last node

    if pos>=0:
        curPtr = ll_head
        for k in range(pos):
            curPtr = curPtr.next
        prevNode.next = curPtr

    return ll_head

def sllLen(ll_head):
    cnt    = 0
    curPtr = ll_head
    while curPtr != None:
        cnt = cnt + 1
        curPtr = curPtr.next
    return cnt

def sll2List(ll_head):
    lout   = []
    curPtr = ll_head
    while curPtr != None:
        lout.append(curPtr.val)
        curPtr = curPtr.next
    return lout

def printSll(ll_head):
    lout = sll2List(ll_head)
    print('printSll: ', lout)    