class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pointer to start and end of list
        leftPointer = 0
        rightPointer = len(numbers) - 1

        # Initialize twoSum
        twoSum = numbers[leftPointer] + numbers [rightPointer]

        # Taking advantage of sorted array
        while twoSum != target:
            if twoSum > target:
                rightPointer -= 1
            else: 
                leftPointer += 1
            twoSum = numbers[leftPointer] + numbers [rightPointer]
            
        # +1 on indices because it's a 1-indexed array
        return [leftPointer + 1, rightPointer + 1]