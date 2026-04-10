class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                threeSum = nums[i] + nums[leftPointer] + nums[rightPointer]

                if threeSum > 0:
                        rightPointer -= 1
                elif threeSum < 0:
                        leftPointer += 1
                else:
                    res.append([nums[i], nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer:
                        leftPointer += 1
        
        return res



