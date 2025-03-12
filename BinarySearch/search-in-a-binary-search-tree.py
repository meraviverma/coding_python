#Defination of tree structure
#for a Binary Tree

class TreeNode:
    #constructor to initialize the Node with a
    #value and set left and right pointer to None

    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    #This function searches for a node with
    # a specified value in a Binary Search Tree (BST).

    def searchBST(self,root,val):
        #Loop until either the tree is
        #Exhausted (None) or the value is found.
        while root is not None and root.val != val:
            # check if the target value is
            # less than the current node's value.
            # If so, move to the left subtree
            # (values smaller than the current node).
            # Otherwise, move to the right subtree
            # (values larger than the current node).
            root=root.left if val < root.val else root.right
        # Return the node containing the target value,
        # if found; otherwise, return None.
        return root

def printInOrder(root):
    # check if the current node

    if root is None:
        return

    printInOrder(root.left)

    print(root.val,end="")

    printInOrder(root.right)


if __name__=="__main__":
    root=TreeNode(5)
    root.left=TreeNode(3)
    root.right=TreeNode(8)
    root.left.left=TreeNode(2)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(6)
    root.right.right=TreeNode(10)

    print("Binary Search Tree: ")
    printInOrder(root)
    print()

    solution=Solution()

    # Searching for a value in BST
    target=6
    result=solution.searchBST(root,target)

    # Display The Search Result
    if result is not None:
        print(f"Value {target} found in the BST!")
    else:
        print(f"Value {target} not found in the BST.")



