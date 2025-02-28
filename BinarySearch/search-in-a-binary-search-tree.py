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
