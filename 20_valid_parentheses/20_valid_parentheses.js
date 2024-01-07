/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let ref = {
    "{": "}",
    "(": ")",
    "[": "]",
  };
  let res = [];
  for (let i = 0; i < s.length; i++) {
    if (ref[s[i]]) res.push(s[i]);
    else {
      if (res.length == 0 || ref[res.pop()] !== s[i]) {
        return false;
      }
    }
  }
  return res.length === 0;
};
