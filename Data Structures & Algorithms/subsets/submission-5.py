class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return
            
            # Include
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

            # Exclude
            backtrack(i+1, path)
        
        backtrack(0, [])

        print(res)

        return res