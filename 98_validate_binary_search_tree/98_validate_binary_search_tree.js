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
 * @return {boolean}
 */
var isValidBST = function (root) {
  // function valid(node, left, right) {
  //     if(!node) return true;

  //     if(node.val <= left || node.val >= right) return false;

  //     return valid(node.left, left, node.val) && valid(node.right, node.val, right)
  // }
  // return valid(root, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY);
  if (!root) {
    return true;
  }

  const stack = [];
  let prev = null;
  while (root || stack.length > 0) {
    while (root) {
      stack.push(root);
      root = root.left;
    }

    root = stack.pop();

    if (prev !== null && root.val <= prev) {
      return false;
    }

    prev = root.val;
    root = root.right;
  }

  return true;
};
