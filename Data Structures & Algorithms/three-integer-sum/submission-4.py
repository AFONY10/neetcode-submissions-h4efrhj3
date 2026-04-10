class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # Outer loop: Pick number as base/first no. in triplet
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            leftPointer = i + 1
            rightPointer = len(nums) - 1

            # While two-pointers havent met/crossed, find valid combination for target
            while leftPointer < rightPointer:
                threeSum = nums[i] + nums[leftPointer] + nums[rightPointer]

                if threeSum > 0:
                        rightPointer -= 1
                elif threeSum < 0:
                        leftPointer += 1
                else:
                    res.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    # For leftPointer, we dont want to reuse same value as previous iteration either
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        
        return res



