# Leetcode 101. Symmetric Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.l = []
        self.r = []
        self.inOrder(root.left)
        self.reverseInOrder(root.right)
        # print(self.l)
        # print(self.r)
        return (self.l==self.r)
            

    def inOrder(self, root):
        if(root):
            if(root.left == None):
                self.l.append(100000)
            if(root.right == None):
                self.l.append(100000)
            
            self.inOrder(root.left)
            self.l.append(root.val)
            self.inOrder(root.right)
    
    
    def reverseInOrder(self, root):
        if(root):
            if(root.left == None):
                self.r.append(100000)
                
            if(root.right == None):
                self.r.append(100000)
            
            self.reverseInOrder(root.right)
            self.r.append(root.val)
            self.reverseInOrder(root.left)