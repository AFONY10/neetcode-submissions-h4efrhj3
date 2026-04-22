class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find correct row with BS
        top, bottom = 0, len(matrix) - 1
        foundRow = []
        while top <= bottom:
            middleRow = (top+bottom) // 2

            
            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottom = middleRow - 1
            else:
                foundRow = matrix[middleRow]
                break

        # Find target in foundRow
        lp = 0
        rp = len(foundRow) - 1

        while lp <= rp:
            mp = (rp+lp) // 2

            if target < foundRow[mp]:
                rp = mp - 1
            elif target > foundRow[mp]:
                lp = mp + 1
            else:
                return True

        return False


