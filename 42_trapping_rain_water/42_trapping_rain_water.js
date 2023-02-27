/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let l = 0
    let r = height.length -1

    let max_l = height[l]
    let max_r = height[r]

    let res = 0
    while(l < r) {
        if(max_l < max_r) {
            l = l +1;
            max_l = height[l] > max_l ? height[l] : max_l
            res = res +  max_l - height[l];
        } else {
            r = r -1;
            max_r = height[r] > max_r ? height[r] : max_r
            res = res + max_r - height[r];
        }
    }

    return res
};
