class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # first
        dic = {}
        for w in wordList:
            dic[w] = []
        
        dic[beginWord] = []
        print(dic)

        def getDiffOne(beginWord):
            ar = []
            for i in range(0, len(beginWord)):
                for word in wordList:    
                    if word == beginWord:
                        continue
                    if beginWord[:i] + beginWord[i + 1:] == word[:i] + word[i + 1:]:
                        ar.append(word)
            return ar

        visited = set()
        res = []
        def dfs(word, count):
            if word == endWord:
                res.append(count)
                return 
            if word in visited:
                return 

            visited.add(word)
            neig = getDiffOne(word)
            print(word, neig, count, visited)
            for n in neig:
                dfs(n, count+1)
            visited.remove(word)
           
        
        dfs(beginWord, 1)
        if len(res) == 0:
            return 0
        return min(res)
