class Node:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                cur.children[i] = Node()
            cur = cur.children[i]
        cur.endOfWord = True
        print("added", word)

    def search(self, word: str) -> bool:
        def dfs(index, node):
            cur = node
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children:
                        if child is not None and dfs(i + 1, child):
                            return True
                    return False  # If no children match
                else:
                    j = ord(c) - ord("a")
                    if cur.children[j] is None:
                        return False
                    cur = cur.children[j]
            return cur.endOfWord

        return dfs(0, self.root)