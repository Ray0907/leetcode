class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        max_f = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] = count[s[r]] +1
            max_f = max(max_f, count[s[r]])
            while (r-l + 1) - max_f > k:
                count[s[l]] = count[s[l]] -1
                l = l +1
            res = max(res, r-l +1)
        return res
