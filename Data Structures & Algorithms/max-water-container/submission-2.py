class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        n = len(heights)
        lp = 0
        rp = n - 1

        while lp < rp:
            currentLength = rp - lp

            if heights[lp] <= heights[rp]:
                currentArea = currentLength*heights[lp]
                if currentArea > maxArea:
                    maxArea = currentArea
                lp += 1
            else:
                currentArea = currentLength*heights[rp]
                if currentArea > maxArea:
                    maxArea = currentArea
                rp -= 1
            
        return maxArea                