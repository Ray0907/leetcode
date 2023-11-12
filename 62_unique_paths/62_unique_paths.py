class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D matrix initialized with 1s, representing paths to each cell
        dp = [[1] * n for i in range(m)]

        # Iterate through the matrix starting from (1,1)
        for i in range(1, m):
            for j in range(1, n):
                # Calculate the number of unique paths to the current cell
                # by adding the paths from the cell above and the cell to the left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # Return the value in the bottom-right cell, which represents
        # the number of unique paths from top-left to bottom-right
        return dp[m - 1][n - 1]
