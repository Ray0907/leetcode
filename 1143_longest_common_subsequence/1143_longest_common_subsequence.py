class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of both input strings
        m, n = len(text1), len(text2)
        
        # Create a 2D matrix initialized with zeros, adding an extra row and column
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill in the matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, increase the LCS length by 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # Otherwise, take the maximum of the left and above cells
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Return the value in the bottom-right cell, which represents the LCS length
        return dp[m][n]
