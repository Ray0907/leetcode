class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Check the least significant bit
            n >>= 1         # Shift right to check the next bit
        return count
        # Brian Kernighan algorithm
        while n:
            n &= (n - 1)  # Turn off the rightmost set bit
            count += 1
        return count