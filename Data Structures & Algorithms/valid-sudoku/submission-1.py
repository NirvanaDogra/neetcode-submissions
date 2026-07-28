class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHashMap = {}
        colHashMap = {}
        subHashMap = {}

        for i in range(0, 9):
            rowHashMap[i] = []
            colHashMap[i] = [] 
           
        # print(colHashMap)
        for i in range(0, 9):
            ar = []
            for j in range(0, 9):
                if board[i][j]!=".":
                    if board[i][j] in ar:
                        return False
                    ar.append(board[i][j])
                    if board[i][j] in colHashMap[j]:
                        return False
                    colHashMap[j].append(board[i][j])

                    
                    print((int(i/3), int(j/3)), board[i][j] )
                    if (int(i/3), int(j/3)) in subHashMap:
                        print(subHashMap[(int(i/3), int(j/3))])
                        if board[i][j] in subHashMap[(int(i/3), int(j/3))]:
                            return False
                        subHashMap[(int(i/3), int(j/3))].append(board[i][j])
                    else:
                        subHashMap[(int(i/3), int(j/3))] = [board[i][j]]
                    
            rowHashMap[i] = ar[:]
      
        return True