class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.lastChar = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord(c) - ord("a")
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.lastChar = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            if index == len(word):
                return root.lastChar
            if word[index] != ".":
                char_index = ord(word[index]) - ord("a")
                if not root.children[char_index]:
                    return False
                return dfs(index + 1, root.children[char_index])
            else:
                for child in root.children:
                    if child and dfs(index + 1, child):
                        return True
                return False
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)