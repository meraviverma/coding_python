"""
Description
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Input: head = [1,2,3,4], index = 1

Output: true

"""

from module.LinkedListDemo import LinkedList
from typing import  Optional
class ListNode:
    def __int__(self):
        self.val=val
        self.next=next
class Solution:
    def hasCycle(self,head:Optional[ListNode])->bool:
        seen=set()
        cur=head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur=cur.next
        return False

if __name__=="__main__":
    obj=LinkedList()
    for val in  [1,2,3,4]:
        obj.insertEnd(val)
    obj.print()