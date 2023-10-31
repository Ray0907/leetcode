class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count =0

        def dfs(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == '1':
                grid[row][col] = 0

                dfs(row -1, col)
                dfs(row +1, col)
                dfs(row, col -1)
                dfs(row, col +1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count = count +1
        return count