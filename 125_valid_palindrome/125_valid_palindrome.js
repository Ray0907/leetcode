/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  s = s.replace(/[^A-Za-z0-9]+/g, "").toLowerCase();
  let l = 0;
  let r = s.length - 1;
  while (r > l) {
    if (s[l] != s[r]) return false;
    l = l + 1;
    r = r - 1;
  }
  return true;
};
