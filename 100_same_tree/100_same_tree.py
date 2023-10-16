# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive
        # if not p and not q:
        #     return True
        # else:
        #     if p and q and p.val == q.val:
        #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        #     else:
        #         return False

        # DFS
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True
        