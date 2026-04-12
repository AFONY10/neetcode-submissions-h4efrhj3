class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        minRes = nums[0]

        while lp <= rp:
            if nums[lp] < nums[rp]:
                minRes = min(minRes, nums[lp])
                break
            
            mp = (lp + rp) // 2
            minRes = min(minRes, nums[mp])

            if nums[mp] >= nums[lp]:
                lp = mp + 1
            else:
                rp = mp - 1
                
        return minRes
