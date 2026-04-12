class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]

        for i in range(len(nums)):
            if nums[i] < minVal:
                minVal = nums[i]
        
        return minVal
