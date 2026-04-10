class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numIndex = {}

        for i, v in enumerate(nums):
            complement = target - v

            if complement in numIndex:
                return [numIndex[complement], i]
            
            numIndex[v] = i
        
        return []


        