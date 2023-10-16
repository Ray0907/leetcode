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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  // function serialize(node) {
  //     if (!node) {
  //         return "null";
  //     }
  //     return "#" + node.val + serialize(node.left) + serialize(node.right);
  // }

  // const rootStr = serialize(root);
  // const subRootStr = serialize(subRoot);

  // return rootStr.includes(subRootStr);
  function isSameTree(tree1, tree2) {
    if (!tree1 && !tree2) {
      return true;
    }
    if (!tree1 || !tree2 || tree1.val !== tree2.val) {
      return false;
    }
    return (
      isSameTree(tree1.left, tree2.left) && isSameTree(tree1.right, tree2.right)
    );
  }

  // 如果當前節點相同，則返回 true
  if (!root) {
    return false;
  }
  if (isSameTree(root, subRoot)) {
    return true;
  }

  // 否則，遞歸檢查左子樹和右子樹
  return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
};
