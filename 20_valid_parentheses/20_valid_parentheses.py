class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_rule = {
            '}': '{',
            ']': '[',
            ')': '(' 
        }

        for c in s:
            if c in dict_rule:
                if stack and stack[-1] == dict_rule[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0 

