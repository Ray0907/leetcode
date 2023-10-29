/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  let result = [];

  function backTrack(remain, current, start) {
    if (remain < 0) return;
    else if (remain == 0) {
      result.push([...current]);
      return;
    } else {
      for (let i = start; i < candidates.length; i++) {
        current.push(candidates[i]);
        backTrack(remain - candidates[i], current, i);
        // 條件不符合所以把最後一個拿掉
        current.pop();
      }
    }
  }
  backTrack(target, [], 0);
  return result;
};
