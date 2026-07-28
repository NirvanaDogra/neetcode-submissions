class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, ptr):

            if ptr == len(word):
                return True
            if (i, j) in visited:
                return False

            if ((i not in range(0, len(board))) or 
               (j not in range(0, len(board[0]))) or
                board[i][j] != word[ptr]):
                return False
                
            print(i, j)
            visited.add((i, j))
            if (dfs(i+1, j, ptr+1) or 
                dfs(i-1, j, ptr+1) or 
                dfs(i, j+1, ptr+1) or 
                dfs(i, j-1, ptr+1)):
                return True
            visited.remove((i, j))
        
            return False
        
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    print("found")
                    visited = set()
                    if(dfs(i, j, 0)):
                        return True
                    
        return False
