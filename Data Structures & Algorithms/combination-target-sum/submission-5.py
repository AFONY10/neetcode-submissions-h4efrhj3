class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, numSum):
            if numSum == target:
                res.append(path.copy())
                return
            
            if i >= len(nums) or numSum > target:
                return
            
            # Include / Reuse
            path.append(nums[i])
            backtrack(i, path, numSum+nums[i])
            path.pop()

            # Exclude / Discard
            backtrack(i+1, path, numSum)
        
        backtrack(0, [], 0)

        return res
        