# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = [root]

        while queue:
            current = []
            next = []

            for node in queue:
                current.append(node.val)

                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            result.append(current)
            queue = next
        return result