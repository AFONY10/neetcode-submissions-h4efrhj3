class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = k * []
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] += 1
            else:
                numFreq[num] = 1
        
        for key, value in sorted(numFreq.items(), key = lambda item : item[1], reverse = True):
            res.append(key)
            if len(res) == k:
                break

        return res        


        