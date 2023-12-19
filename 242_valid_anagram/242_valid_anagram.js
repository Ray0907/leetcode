/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  let dict_1 = {};
  let dict_2 = {};

  for (let char of s) {
    dict_1[char] = (dict_1[char] || 0) + 1;
  }

  for (let char of t) {
    dict_2[char] = (dict_2[char] || 0) + 1;
  }

  for (let key of Object.keys(dict_1)) {
    if (!dict_2[key] || dict_1[key] !== dict_2[key]) {
      return false;
    }
  }
  return true;
};
