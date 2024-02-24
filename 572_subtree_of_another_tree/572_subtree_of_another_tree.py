# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:  # If root is None, return False
            return False
        # Check if the current subtree starting at root matches subRoot
        return self.isSameTree(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)

    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:  # Both trees are empty, hence same
            return True
        if not root1 or not root2:  # One of the trees is empty, not same
            return False
        # Check if current nodes have the same value and if subtrees are same
        return root1.val == root2.val and \
               self.isSameTree(root1.left, root2.left) and \
               self.isSameTree(root1.right, root2.right)
