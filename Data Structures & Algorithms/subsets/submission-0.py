class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        def backtrack(i, path):
            if i >= len(nums):
                self.res.append(path.copy())
                return

            currNum = nums[i]

            # If include
            self.path.append(currNum)
            backtrack(i+1, self.path)

            # if exclude
            self.path.pop()
            backtrack(i+1, self.path)
        
        backtrack(0, self.path)

        return self.res