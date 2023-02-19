class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t): return False
        dict_s = {}
        dict_t = {}
        for i in s:
            if not i in  dict_s: dict_s[i] = 1
            else: dict_s[i] = dict_s[i] + 1
        for i in t:
            if not i in dict_t: dict_t[i] = 1
            else: dict_t[i] = dict_t[i] + 1
        return dict_t == dict_s
