class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c == '.':
                    for child in node.children:
                        if(search_in_node(word[i+1:], node.children[child])):
                            return True
                    return False
                elif c not in node.children:
                    return False
                node = node.children[c]
            return node.isEndOfWord
        return search_in_node(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)