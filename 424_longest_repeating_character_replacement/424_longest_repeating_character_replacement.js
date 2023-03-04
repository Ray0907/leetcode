/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let count = {};
    res = 0

    l =0;
    max_f = 0;

    for(let r=0; r< s.length; r++) {
        if(s[r] in count) {
            count[s[r]] = count[s[r]] + 1;
        }
        else {
            count[s[r]] = 1;
        }
        max_f = max_f > count[s[r]] ? max_f: count[s[r]];
        while (r- l + 1 - max_f > k) {
            count[s[l]] = count[s[l]] -1;
            l = l +1;
        }
        res = res > r-l +1 ? res: r-l +1
    }
    return res;

};
