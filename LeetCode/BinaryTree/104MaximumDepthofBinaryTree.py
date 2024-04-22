#!/bin/python3
# DONE
# 17.04.2024

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        # +1 for root node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        