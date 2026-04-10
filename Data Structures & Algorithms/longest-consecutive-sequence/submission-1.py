class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if this number is the start of a sequence
            if num - 1 not in numSet:
                currentNum = num
                currentLength = 1

                # keep going while the next number exists
                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentLength += 1

                if currentLength > longest:
                    longest = currentLength

        return longest