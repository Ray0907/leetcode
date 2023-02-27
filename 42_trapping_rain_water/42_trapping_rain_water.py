class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) == 0: return []
        l = 0
        r = len(height) -1

        max_l = height[l]
        max_r = height[r]
        while l < r:
            if max_l < max_r:
                l = l+1
                max_l = max(height[l], max_l)
                res = res + max_l - height[l]
            else:
                r = r-1
                max_r = max(height[r], max_r)
                res = res + max_r - height[r]
        return res

