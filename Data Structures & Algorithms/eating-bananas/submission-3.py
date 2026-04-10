class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxK = 0
        n = len(piles)

        # Compute maxK (could also have used: maxK = max(piles))
        for i in range(n):
            if piles[i] > maxK:
                maxK = piles[i]
        
        lp = 1
        rp = maxK
        res = rp
        while lp <= rp:
            k = (lp+rp) // 2
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k
            
            if hours <= h:
                res = min(res, k)
                rp = k - 1
            else:
                lp = k + 1
                
                
        return res