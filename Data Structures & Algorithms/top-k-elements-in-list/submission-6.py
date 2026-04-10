class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fqRes = []
        fqCounter = OrderedDict()
        # Constructing fqCounter Dict to have all distrinct numbers and their frequeincies mapped in key-value pairs
        for n in nums:
            if n in fqCounter:
                fqCounter[n] += 1
            else:
                fqCounter[n] = 1
        
        # Sort the dictionary items by value (frequency) in descending order
        sorted_items = sorted(fqCounter.items(), key=lambda item: item[1], reverse=True)
        
        loopCounter = 0

        for key, val in sorted_items:
            if loopCounter == k:
                 return fqRes
            else:
                fqRes.append(key)
            loopCounter += 1
            
    
        return fqRes