# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ar = [root]
        lst = []
        
        while len(ar) > 0:
            temp = []
            next_level = []
            
            for node in ar:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            lst.append(temp)
            ar = next_level  # Move to the next level
        
        return lst