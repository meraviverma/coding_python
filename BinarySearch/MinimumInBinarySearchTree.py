# Python code to find minimum value in BST
# using inorder traversal
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inorder(root,sorted_inorder):

    #Base Case
    if root is None:
        return

    #Traverse left subtree
    inorder(root.left,sorted_inorder)

    #Store the current node's data
    sorted_inorder.append(root.data)

    #Traverse right subtree
    inorder(root.right,sorted_inorder)

def minValue(root):
    if root is None:
        return -1

    #Using a list to hold inorder elements
    sorted_inorder=[]

    #call the recursive inorder function
    inorder(root,sorted_inorder)

    #Return  the first element, which is the minimum
    return sorted_inorder[0]

if __name__=="__main__":

    # Representation of input binary search tree
    #        5
    #       / \
    #      4   6
    #     /     \
    #    3       7
    #   /
    #  1
    root=Node(5)
    root.left=Node(4)
    root.right=Node(6)
    root.left.left=Node(3)
    root.right.right=Node(7)
    root.left.left.left=Node(1)


    print(minValue(root))

