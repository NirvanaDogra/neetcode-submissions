class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            result = list(filter(lambda x: x != '.', row))
            if len(result) != len(set(result)):
                print("failing row", result)
                return False
        
        for i in range(0, len(board)):
            col = [row[i] for row in board]
            result = list(filter(lambda x: x != '.', col))
            if len(result) != len(set(result)):
                print("failing col", result)
                return False
        

        for k in range(0, len(board[0]), 3):
            for l in range(0, len(board[0]), 3):
                ar = [row[l:l+3] for row in board[k:k+3]]
                print(ar)
                allInOne =[]
                for row in ar:
                    allInOne = allInOne+row
                result = list(filter(lambda x: x != '.', allInOne))
                if len(result) != len(set(result)):
                    print("filed", ar)
                    return False
                # else:
                #     return True
                # break
        return True



