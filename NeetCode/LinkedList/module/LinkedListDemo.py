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
        """
                Initializes a node with the given value and sets the next pointer to None.

                Args:
                    val (int): The value stored in this node.
        """

        self.val=val
        self.next=None

class LinkedList:
    #At the beginning, both head and tail point to the same dummy node:
    def __init__(self):
        """
        Initializes a new singly linked list with a dummy head node.
        This dummy node simplifies edge case handling, especially when
        inserting or deleting at the head of the list.
        """

        self.head=ListNode(-1) # Dummy node for simplification
        self.tail=self.head # Initially, tail is also the dummy node

    def insertEnd(self,val):
        """
        Appends a new node with the given value at the end of the list.

        Args:
            val (int): Value to insert into the list.
        """

        self.tail.next=ListNode(val)
        self.tail=self.tail.next

    def remove(self,index):
        """
        Removes the node at the specified index (0-based).
        If the index is invalid (too large), the function performs no operation.

        Args:
            index (int): The index of the node to remove.
        """

        i=0
        curr=self.head
        # Traverse to the node just before the one to be removed

        while i < index and curr:
            i+=1
            curr=curr.next

        #remove the node ahead of error
        # Remove the node if it exists
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr # Update tail if removing last node
            curr.next=curr.next.next
    def print(self):
        """
        Prints the list in a readable 'value -> value ->' format.
        Skips the dummy head node and prints from the first actual element.
        """

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


