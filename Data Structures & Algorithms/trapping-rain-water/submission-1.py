class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        for i in range(1, n-1):
            maxLeft = 0
            maxRight = 0
            # Max height to the left:
            for l in range(i-1, -1, -1):
                if height[l] > maxLeft:
                    maxLeft = height[l]
            
            for r in range(i+1, n, 1):
                if height[r] > maxRight:
                    maxRight = height[r]
            
            print(maxLeft, maxRight)

            currentWater = min(maxLeft, maxRight) - height[i]

            if currentWater > 0:
                water += currentWater

        return water