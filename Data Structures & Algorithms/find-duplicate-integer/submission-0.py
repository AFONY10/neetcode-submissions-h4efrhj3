class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for i in range(0, n):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])
        
        return 0
