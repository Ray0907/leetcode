class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def can_break(s):
            if s in memo:
                return memo[s]
            if not s:
                return True
            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in word_set and can_break(s[i:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        
        return can_break(s)
