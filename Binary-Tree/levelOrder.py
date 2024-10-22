# Leetcode 102. Binary Tree Level Order Traversal

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = deque()
        level.append(root)
        t = []
        while level:
            x = []
            size = len(level)
            for _ in range(size):
                node = level.popleft()
                x.append(node.val)
                if (node.left):
                    level.append(node.left)
                if (node.right):
                    level.append(node.right)
            t.append(x)
        return t