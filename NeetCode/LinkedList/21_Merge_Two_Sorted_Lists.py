"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
from typing import Optional


class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkList:
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=self.head
    def insertEnd(self,val):
        self.tail.next=ListNode(val)
        self.tail=self.tail.next
    #You're telling Python not to move to the next line after printing.
    # That way, all the values in the linked list appear side by side on the same line like:
    def print(self):
        curr=self.head.next
        while curr:
            print(curr.val,"--->",end="") #In Python, the print() function automatically adds a newline (\n) at
            # the end of each output by default.
            # But with end="", you're overriding that behavior. In your line:
            curr=curr.next
        print()

    def mergeTwoLists(self,list1:Optional[ListNode],list2:Optional[ListNode])-> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 in None:
            return list2
        if list1.val <= list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2


if __name__=="__main__":
    obj=LinkList()
    obj.insertEnd(1)
    obj.insertEnd(2)
    obj.insertEnd(4)

    obj.print()

    obj2=LinkList()
    obj2.insertEnd(1)
    obj2.insertEnd(3)
    obj2.insertEnd(4)
    obj2.insertEnd(9)
    obj2.print()

    abc=LinkList()
    mylist=abc.mergeTwoLists(obj,obj2)




