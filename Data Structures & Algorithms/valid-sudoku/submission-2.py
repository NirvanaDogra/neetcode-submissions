class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashMap = defaultdict(set)
        colHashMap = defaultdict(set)
        subHashMap = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]== '.':
                    continue
                if (board[r][c] in rowHashMap[r] or board[r][c] in colHashMap[c] or board[r][c] in subHashMap[(r//3, c//3)]):
                    return False
                
                rowHashMap[r].add(board[r][c])
                colHashMap[c].add(board[r][c])
                subHashMap[(r//3, c//3)].add(board[r][c])
                 
        return True