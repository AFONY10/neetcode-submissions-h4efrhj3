# 1. [1, 1, 1, 6, 7, 5, 1, 3] n = 8, highest single = 8
# 2. 

# heights = [7, 1, 7, 2, 2, 4], output= 8
    # 1. 4 added to stack - maximum area = min(stack)*len(stack)
    # 2. 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        n = len(heights)
        for i, currH in enumerate(heights):
            start = i
            while stack and stack[-1][1] > currH:
                start, val = stack.pop()

                currArea = val * (i-start)
                res = max(res,currArea)

            stack.append((start, currH))

        for i, h in stack:
            res = max(res, h*(len(heights)-i))

        
        return res

