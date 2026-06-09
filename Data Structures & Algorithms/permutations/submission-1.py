class Solution:
        def permute(self, nums: List[int]) -> List[List[int]]:
                res = []

                def backtrack(permutation, visited):
                        if len(permutation) == len(nums):
                                res.append(permutation.copy())
                                return
                        
                        for i in range(len(nums)):
                                if not visited[i]:
                                        permutation.append(nums[i])
                                        visited[i] = True
                                        backtrack(permutation, visited)
                                        permutation.pop()
                                        visited[i] = False
                        
                backtrack([], [False] * len(nums))

                return res
