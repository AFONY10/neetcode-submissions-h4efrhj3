class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        sqr = {}
        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == '.':
                    continue
                
                # Index of square
                square = (r//3)*3+c//3
                if r not in row:
                    row[r] = set()
                if c not in col:
                    col[c] = set()
                if square not in sqr:
                    sqr[square] = set()

                if current in row[r] or current in col[c] or current in sqr[square]:
                    return False
                
                row[r].add(current)
                col[c].add(current)
                sqr[square].add(current)
        
        return True