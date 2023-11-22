# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:35:11 2023

@author: brigh
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
            
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
        
    return dummy.next


if __name__ == '__main__':
    a = [1,2,4]; b = [1,3,4,5]
    node1 = ListNode(a[0])
    node2 = ListNode(a[1])
    node3 = ListNode(a[2])
    
    node4 = ListNode(b[0])
    node5 = ListNode(b[1])
    node6 = ListNode(b[2])
    node7 = ListNode(b[3])
    
    x = mergeTwoLists(node1, node4)
    print(x)