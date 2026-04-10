# 1. Container to detect duplicate: set()
# 2. Remove duplicate: [0, 1, 1, 2] -> [0, 1, 2]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set() # (2, 10)
        lp = 0 # 3
        rp = len(nums) # 5

        while lp < rp: # 3 < 5 = True
            if nums[lp] in seen: # nums[3] = 30 in set = False
                nums.pop(lp) # nums=[2,10,30,30,30] , 
                rp -= 1
                continue
                # duplciate remove
            else:
                seen.add(nums[lp])
            lp += 1
        
        return len(nums)
            

