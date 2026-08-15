class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
   
        while len(stones) > 1:
            n = len(stones)
            difference = stones[n-1] - stones[n-2]
            if difference == 0:
                stones.pop()
                stones.pop()
            else:
                val = stones.pop()
                stones[n-2] = val - stones[n-2]
            stones.sort()
        
        if stones:
            return stones[-1]
        else:
            return 0