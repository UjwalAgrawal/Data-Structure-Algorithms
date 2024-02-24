# Leetcode 199. Binary Tree Right Side View

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
    return [item[-1] for item in t]       
            

