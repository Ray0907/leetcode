/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let char_set = new Set();
    let l = 0;
    let res = 0;

    for(let r=0; r< s.length; r++) {
        while(char_set.has(s[r])) {
            char_set.delete(s[l]);
            l = l +1
        }
        char_set.add(s[r]);
        res = res > r - l + 1 ? res: r-l+1;
    }
    return res;
};
