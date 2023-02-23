/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let items = []

    let prefix = 1
    let postfix = 1

    for(let i=0; i< nums.length; i++) {
        items[i] = prefix;
        prefix = prefix * nums[i];
    }

    for(let i=nums.length-1 ; i>= 0; i--) {
        items[i] = items[i] * postfix;
        postfix = postfix * nums[i];
    }
    return items
};
