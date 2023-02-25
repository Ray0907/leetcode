class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            if(num-1 not in data):
                length = 1
                while num + length in data:
                    length = length +1
                longest = max(longest, length)
        return longest
