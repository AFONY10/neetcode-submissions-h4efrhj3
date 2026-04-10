# Bruteforce:
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0

        # Checking how much water every position can trap
        for i in range(1, n-1):
            maxLeft = 0
            maxRight = 0

            # Max height to the left from current position
            for l in range(i-1, -1, -1):
                if height[l] > maxLeft:
                    maxLeft = height[l]

            # Max height to the right from current position
            for r in range(i+1, n, 1):
                if height[r] > maxRight:
                    maxRight = height[r]
            
            # Calculating value for how much water can be trapped in current position
            currentWater = min(maxLeft, maxRight) - height[i]

            # If 0 or less, we dont increment variable
            if currentWater > 0:
                water += currentWater

        return water