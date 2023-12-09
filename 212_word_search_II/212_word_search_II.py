class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row, col, word, node):
            if not (0 <= row < len(board)) or not (0 <=col < len(board[0])) or board[row][col] == '#': return False

            letter = board[row][col]
            new_word = word + letter
            if letter not in node: return False
            
            if 'end' in node[letter]: result.add(new_word)

            original_letter = board[row][col]
            board[row][col] = '#'

            for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]: dfs(row+ dr, col + dc, new_word, node[letter])

            board[row][col] = original_letter
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['end'] = True
        result = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j ,'', trie)
        return list(result)