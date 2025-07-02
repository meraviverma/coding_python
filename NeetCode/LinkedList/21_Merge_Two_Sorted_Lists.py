from typing import Optional

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = ListNode(-1)  # dummy head
        self.tail = self.head

    def insertEnd(self, val: int):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, "--->", end="")
            curr = curr.next
        print()

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def printList(head: Optional[ListNode]):
    curr = head
    while curr:
        print(curr.val, "--->", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    obj1 = LinkList()
    for val in [1, 2, 4]:
        obj1.insertEnd(val)
    obj1.print()

    obj2 = LinkList()
    for val in [1, 3, 4, 9]:
        obj2.insertEnd(val)
    obj2.print()

    mergedHead = mergeTwoLists(obj1.head.next, obj2.head.next)
    print("Merged List:")
    printList(mergedHead)