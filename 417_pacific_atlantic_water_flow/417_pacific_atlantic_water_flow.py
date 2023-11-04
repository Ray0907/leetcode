class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        row_length = len(heights)
        col_length = len(heights[0])

        pacific_reachable = [[False] * col_length for i in range(row_length)] 
        atlantic_reachable = [[False] * col_length for i in range(row_length)]

        def dfs(row, col, reachable):
            reachable[row][col] = True

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                r = row + dr
                c = col + dc

                if 0 <= r < row_length and 0 <= c < col_length and not reachable[r][c] and heights[r][c] >= heights[row][col]:
                    dfs(r, c, reachable)
        # From edge to center
        for row in range(row_length):
            dfs(row, 0, pacific_reachable)
        for col in range(col_length):
            dfs(0, col, pacific_reachable)

        for row in range(row_length):
            dfs(row, col_length-1, atlantic_reachable)
        for col in range(col_length):
            dfs(row_length-1 , col, atlantic_reachable)
        
        result = []
        for i in range(row_length):
            for j in range(col_length):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i,j])
        return result