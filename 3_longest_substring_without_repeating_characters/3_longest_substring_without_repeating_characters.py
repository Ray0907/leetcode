class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_char = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in set_char:
                set_char.remove(s[l])
                l = l +1
            set_char.add(s[r])
            res = max(res, r-l + 1)
        return res
