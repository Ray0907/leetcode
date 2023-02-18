var containsDuplicate = function(nums) {
    let flag = (new Set(nums)).size != nums.length ? true : false;
    return flag
};
