class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            lp = 0
            rp = len(row) - 1

            while lp <= rp:
                mp = (lp + rp) // 2

                if row[mp] == target:
                    return True
                elif row[mp] < target:
                    lp = mp + 1
                else:
                    rp = mp - 1
        return False 