# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    #     if not tree1 and not tree2:
    #         return True
    #     if not tree1 or not tree2 or tree1.val != tree2.val:
    #         return False
    #     return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)
    
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return False
    #     if self.isSameTree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "null"
            return "#" + str(node.val) + serialize(node.left) + serialize(node.right)

        root_str = serialize(root)
        subRoot_str = serialize(subRoot)

        return subRoot_str in root_str
        