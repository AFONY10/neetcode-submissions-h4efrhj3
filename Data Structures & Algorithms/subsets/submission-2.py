class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path = []
        self.res = []
        self.n = len(nums)
        def backtrack(i):
            if i >= self.n:
                self.res.append(self.path.copy())
                return
            
            currNum = nums[i]

            # If append
            self.path.append(currNum)
            backtrack(i+1)
            self.path.pop()

            # If not append
            backtrack(i+1)
        
        backtrack(0)

        return self.res
