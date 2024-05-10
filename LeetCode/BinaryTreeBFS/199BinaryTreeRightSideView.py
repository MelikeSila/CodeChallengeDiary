# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        rightNodeArray = []
        temp = root
        

        while temp:
            rightNodeArray.append(temp.val)
            temp = temp.right
        
        if len(rightNodeArray) == 1 and root.left != None:
            rightNodeArray.append(root.left.val)

        return rightNodeArray