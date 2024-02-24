# Leetcode 102. Binary Tree Level Order Traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        level = [root]
        t = []
        while(level):
            x = []
            for i in range(len(level)):
                node = level.pop(0)
                x.append(node.val)
                if(node.left):
                    level.append(node.left)
                if(node.right):
                    level.append(node.right)
            t.append(x)
        return t
        