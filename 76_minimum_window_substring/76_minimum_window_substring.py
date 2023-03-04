class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        target = {}

        for i in range(len(t)):
            if(t[i] not in target):
                target[t[i]] = 1
            else :
                target[t[i]] = target[t[i]] + 1
        have, need = 0, len(target)
        res, resLen = [-1, -1], float('infinity')

        window = {}
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in target and window[c] == target[c]:
                have +=1
            
            while have == need:
                if(r-l +1) < resLen:
                    res = [l, r]
                    resLen = r-l +1
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l +=1

        l, r = res
        return s[l:r+1] if resLen != float('infinity') else  ''
