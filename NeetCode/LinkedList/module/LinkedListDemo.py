"""
Linked Lists have a head, and a tail pointer. The head pointer points to the very first node in the linked list,
ListNode1, and the tail pointer points to the very last node — ListNode3.
If there is only one node in the Linked List, the head and the tail point to the same node.

If we want to insert listnode4 to the end tail.next=ListNode4
tail=tail.next
or
tail=ListNode4
"""
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    #At the beginning, both head and tail point to the same dummy node:
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    def insertEnd(self,val):
        self.tail=val
