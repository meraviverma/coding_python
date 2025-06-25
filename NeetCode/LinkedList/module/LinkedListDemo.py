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
        self.tail.next=ListNode(val)
        self.tail=self.tail.next

    def remove(self,index):
        i=0
        curr=self.head
        while i < index and curr:
            i+=1
            curr=curr.next

        #remove the node ahead of error
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next=curr.next.next
    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val,"-->",end="")
            curr=curr.next
        print()
if __name__=="__main__":
    obj=LinkedList()
    obj.insertEnd(5)
    obj.insertEnd(10)
    obj.insertEnd(20)
    obj.insertEnd(2)
    obj.insertEnd(99)
    obj.print()
    obj.remove(3)
    obj.print()
    # 5 -->10 -->20 -->2 -->99 -->
    # 5 -->10 -->20 -->99 -->


