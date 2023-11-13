/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let max_reach = 0;

  for (let i = 0; i < nums.length; i++) {
    if (i > max_reach) return false;
    max_reach = Math.max(max_reach, i + nums[i]);
    if (max_reach >= nums.length - 1) return true;
  }
  return false;
};
