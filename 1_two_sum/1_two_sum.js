/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let dict = {};
  for (let i = 0; i < nums.length; i++) {
    let diff = target - nums[i];
    if (dict.hasOwnProperty(diff)) {
      return [i, dict[diff]];
    } else dict[nums[i]] = i;
  }
};
