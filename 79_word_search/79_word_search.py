class Solution:
    def exist(self, board, word):
        def dfs(i, j, k):
            # Boundary conditions and mismatch with characters
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])) or board[i][j] != word[k]:
                return False
            # If we've matched the last character of the word, we've found it
            if k == len(word) - 1:
                return True
            # Mark the current cell as visited
            tmp, board[i][j] = board[i][j], '/'
            # Try to continue searching for the next character in four directions
            res = dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1)
            # Restore the current cell
            board[i][j] = tmp
            return res

        # Traverse the entire character grid
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Start searching for the word from each cell
                if dfs(i, j, 0):
                    return True
        return False