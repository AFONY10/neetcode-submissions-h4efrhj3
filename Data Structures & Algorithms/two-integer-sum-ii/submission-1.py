class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indexVals = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in indexVals:
                return [indexVals[complement]+1, i+1]
            
            indexVals[num] = i