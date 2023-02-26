class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # Skip positive integers
            if num > 0 :break
            if i > 0 and num == nums[i -1]:
                continue
            l = i +1
            r = len(nums) -1
            while l< r:
                ans = num + nums[l] + nums[r]
                if ans > 0:
                    r = r-1
                elif ans < 0:
                    l = l +1
                else:
                    res.append([num, nums[l], nums[r]])
                    l = l +1
                    r = r -1
                    while nums[l] == nums[l-1] and l < r:
                        l = l+1
        return res
