class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in valueToIndex:
                return [valueToIndex[complement], i]
            else:
                valueToIndex[num] = i
            
        return []