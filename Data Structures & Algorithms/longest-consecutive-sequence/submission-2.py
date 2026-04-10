class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seq = set(nums)

        for num in seq:
            currentLength = 1
            currentNumber = num
            
            while currentNumber+1 in seq:
                currentNumber += 1
                currentLength += 1
            
            if currentLength > longest:
                longest = currentLength
        
        return longest

            
            
