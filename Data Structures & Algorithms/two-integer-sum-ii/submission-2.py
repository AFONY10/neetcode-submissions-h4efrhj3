class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        leftPointer = 0
        rightPointer = len(numbers) - 1

        twoSum = numbers[leftPointer] + numbers [rightPointer]

        while twoSum != target:
            if twoSum > target:
                rightPointer -= 1
            else: 
                leftPointer += 1
            twoSum = numbers[leftPointer] + numbers [rightPointer]
        return [leftPointer + 1, rightPointer + 1]