class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        sqr = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if (r // 3, c//3) not in sqr:
                    sqr[(r // 3, c // 3)] = set()

                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in sqr[(r//3, c//3)]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sqr[(r//3, c//3)].add(board[r][c])
        return True


