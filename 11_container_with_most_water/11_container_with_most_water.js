/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let area = 0
    let l = 0
    let r = height.length -1

    let res = 0
    while(l < r) {
        let length = height[l] < height[r] ? height[l]: height[r]
        area =  length * (r-l)
        res = area > res ? area: res
        if(height[l] > height[r]) {
            r = r-1
        } else {
            l = l+1
        }
    }
    return res
};
