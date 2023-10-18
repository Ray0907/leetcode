class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
    
        for i in range(1, n + 1):
            # To count the number of 1's in binary representation of i,
            # use the formula: ans[i] = ans[i >> 1] + (i & 1)
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans