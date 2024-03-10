class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        
        # Iterate from 1 to n
        for i in range(1, n + 1):
            # Use the previously computed result for i // 2
            # Add 1 if i is odd, else just use the count for i // 2
            result[i] = result[i // 2] + (i % 2)
        
        return result
