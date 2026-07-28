# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True
        def dfs(p, q):
            print(p, q)
            if not self.isSame:
                return 0
            if not p and q:
                self.isSame = False
                return 0
            if p and not q:
                self.isSame = False
                return 0

            if not p and not q:
                return 0

            if p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            else:
                self.isSame = False
                return 0

        dfs(p, q)
        return self.isSame

                
