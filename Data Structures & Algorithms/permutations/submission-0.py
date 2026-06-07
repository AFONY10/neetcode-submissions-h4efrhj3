class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        permutations = []
        def backtrack(path, visited):
            if len(permutations) == len(nums):
                res.append(permutations.copy())
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(path, visited)
                    path.pop()
                    visited[i] = False

        
        backtrack(permutations, visit)

        return res
