# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive
        if not root:
            return None

        root.left, root.right = root.right , root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        # iterative
        stack = [root]

        while stack:
            node = stack.pop()

            # Swap the left and right children
            node.left, node.right = node.right, node.left

            # Add non-empty child nodes to the stack
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root