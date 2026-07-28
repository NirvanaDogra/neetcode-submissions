# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left = 0
        right = 0

        def getHeight(root):
            print("yes")
            if not root:
                return 0
            
            
            # print(left, right)
            left=1+getHeight(root.left)
            right=1+getHeight(root.right)
            

            return max(left, right)

        return getHeight(root)