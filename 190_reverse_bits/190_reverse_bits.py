class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1  # Left shift result by 1 position
            result |= (n >> i) & 1  # Add the current bit to result
        return result