class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0
        n = len(heights)
        for i in range(n):
            lp = i
            rp = i

            while lp-1 >= 0 and heights[lp-1] >= heights[i]:
                lp -= 1
            print(lp)
            while rp+1 < n and heights[rp+1] >= heights[i]:
                rp += 1
            print(rp)
            currWidth = rp - lp + 1
            currArea = currWidth * heights[i]
            print("It:", i, "CurrWidth", currWidth, "CurrArea", currArea)
            if currArea > res:
                res = currArea
            
        return res



