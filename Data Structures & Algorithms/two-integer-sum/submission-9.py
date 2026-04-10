class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in numIndex:
                return [numIndex[target-nums[i]], i]
            numIndex[nums[i]] = i
        
        return []