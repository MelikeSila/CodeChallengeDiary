# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        import math
        
        head = TreeNode()
        tree = head
        i = len(nums)//2

        tree.val = nums[i]
        
        if len(nums[0:i]):
            tree.left = self.sortedArrayToBST(nums[0:i])
        if nums[i+1:]:
            tree.right = self.sortedArrayToBST(nums[i+1:])

        return head