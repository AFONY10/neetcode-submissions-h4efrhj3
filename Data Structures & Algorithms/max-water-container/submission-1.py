class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = set()

        leftPointer = 0
        rightPointer = len(heights) - 1

        while leftPointer < rightPointer:
            currentLength = rightPointer - leftPointer
            
            if heights[leftPointer] <= heights[rightPointer]:
                currentArea = currentLength * heights[leftPointer]
                areas.add(currentArea)
                print(areas)
                leftPointer += 1
            else:
                currentArea = currentLength * heights[rightPointer]
                areas.add(currentArea)
                rightPointer -= 1
        
        return max(areas)