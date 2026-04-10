class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        if nums[lp] == target:
            return lp

        if nums[rp] == target:
            return rp

        while lp <= rp:
            midPointer = int((lp + rp)/2)
            print(lp, rp, midPointer)

            if nums[midPointer] == target:
                return midPointer
            elif nums[midPointer] < target:
                lp = midPointer + 1
                continue
            else:
                rp = midPointer - 1
                continue
        
        return -1
