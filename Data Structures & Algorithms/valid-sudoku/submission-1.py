class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                elif digit in seen:
                    return False
                seen.add(digit)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                elif digit in seen:
                    return False
                seen.add(digit)

        # Check 3x3 squares
        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                seen = set()
                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        digit = board[row][col]
                        if digit == ".":
                            continue
                        elif digit in seen:
                            return False
                        seen.add(digit)

        return True