/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

// Recursive
var maxDepth = function (root) {
  if (root === null) return 0;
  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};

var maxDepth = function (root) {
  if (root === null) return 0;

  let left_depth = maxDepth(root.left);
  let right_depth = maxDepth(root.right);

  return Math.max(left_depth, right_depth) + 1;
};
