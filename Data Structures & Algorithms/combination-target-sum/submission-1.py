class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        def backtrack(i, path, numSum):
            if numSum == target:
                self.res.append(path.copy())
                return
            
            if numSum > target or i >= len(nums):
                return
            
            numSum += nums[i]

            # Include current
            path.append(nums[i])
            backtrack(i, path, numSum)
            numSum -= nums[i]
            path.pop()

            # Exclude curent
            backtrack(i+1, path, numSum)
        
        backtrack(0, [], 0)

        return self.res