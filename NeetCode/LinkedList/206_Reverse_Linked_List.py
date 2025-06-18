"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Input: head = [0,1,2,3]

Output: [3,2,1,0]


"""
from typing import Optional
from NeetCode.LinkedList.module.LinkedList import LinkedList


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseLinkedList(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head:
            return None
        newHead=head
        if head.next:
            newHead = self.reverseLinkedList(head.next)
            head.next.next=head
        head.next=None

        return newHead

    def print_linked_list(self,head: Optional[ListNode]):
        curr = head
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print("None")

if __name__=="__main__":
    mylinklist= LinkedList()
    mylinklist.insertEnd(0)
    mylinklist.insertEnd(1)
    mylinklist.insertEnd(2)
    mylinklist.insertEnd(3)

    mylinklist.print()

    obj=Solution()
    #print(input)
    newlinklist=obj.reverseLinkedList(mylinklist.head.next)

    obj.print_linked_list(newlinklist)