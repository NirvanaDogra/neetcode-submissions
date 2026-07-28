# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        levelNode = []
        
        while len(queue) > 0:
            copyQueue = queue[:]
            levelLst = []
            for node in copyQueue:
                temp = queue.pop(0)
                levelLst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(levelLst[-1])
            levelNode.append(levelLst[-1])
        
        
        return levelNode

