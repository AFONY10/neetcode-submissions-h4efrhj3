class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            currNum = nums[i]

            # If include
            path.append(currNum)
            backtrack(i + 1, path)
            path.pop()

            # If exclude
            backtrack(i + 1, path)
        
        backtrack(0, [])

        return res

            
