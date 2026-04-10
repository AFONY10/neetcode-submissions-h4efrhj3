class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lp = 0
        rp = n-1
        maxRight = height[rp]
        maxLeft = height[lp]
        waterRes = 0
        while lp < rp:
            if maxLeft <= maxRight:
                lp += 1
                if maxLeft < height[lp]:
                    maxLeft = height[lp]
                waterRes += maxLeft - height[lp]   
            else:
                rp -= 1
                if maxRight <= height[rp]:
                    maxRight = height[rp]
                waterRes += maxRight - height[rp]

        return waterRes