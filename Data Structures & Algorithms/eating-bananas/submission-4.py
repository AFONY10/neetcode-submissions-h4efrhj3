class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find max k to make our range
        maxK = 0
        for i in range(len(piles)):
            if piles[i] > maxK:
                maxK = piles[i]
            
        lp = 1
        rp = maxK
        k = maxK

        while lp <= rp:
            currentK = (rp + lp) // 2
            hours = 0

            # Calculating hours it'd take to finish pile with currentK
            for pile in piles:
                hours += math.ceil(pile/currentK)

            if hours <= h:
                k = min(k, currentK)
                rp = currentK - 1
            else:
                lp = currentK + 1
            
            
        
        return k
            



            
            
