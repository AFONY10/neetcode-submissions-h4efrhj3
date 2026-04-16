class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lp = 0
        rp = lp + k - 1
        n = len(nums)
        res = []

        while rp < n:
            res.append(max(nums[lp:rp+1]))

            rp += 1
            lp += 1
        
        return res

