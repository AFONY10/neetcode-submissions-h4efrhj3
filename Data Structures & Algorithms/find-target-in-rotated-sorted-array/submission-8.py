class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        indexReturn = -1

        if nums[lp] == target:
            return lp
        
        if nums[rp] == target:
            return rp
        
        while lp <= rp:
            mp = (lp + rp) // 2
            if nums[mp] == target:
                    return mp
            
            # If we are in a singular sorted portion (n rotwations)
            if nums[lp] < nums[rp]:
                if nums[mp] <= target:
                    lp = mp + 1
                else:
                    rp = mp - 1
                continue
            
            # If we are in left-sorted portion
            elif nums[mp] >= nums[lp]:
                if nums[mp] < target or target < nums[lp]:
                    lp = mp + 1
                else:
                    rp = mp - 1

            # If we are in right-sorted portion
            else:
                if nums[mp] > target or target > nums[rp]:
                    rp = mp - 1
                else:
                    lp = mp + 1

        return indexReturn