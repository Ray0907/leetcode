class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n  # Initialize missing as n because the missing number could be n.

        for i in range(n):
            missing ^= i ^ nums[i]  # Use XOR to update the missing number.

        return missing