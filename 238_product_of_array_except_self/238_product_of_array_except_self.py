class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        items = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            items[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            items[i] = items[i] * postfix
            postfix = postfix * nums[i]
        return items
