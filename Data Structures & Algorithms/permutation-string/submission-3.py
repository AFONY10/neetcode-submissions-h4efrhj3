class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Hashtable construction for comparison
        s1Count = {}
        s2Count = {}
        for i in range(len(s1)):
            if s1[i] in s1Count:
                s1Count[s1[i]] += 1
            else:
                s1Count[s1[i]] = 1
        
        # 2. Comparing s2 with s1 Hashtable
        lp = 0
        validSize = len(s1)
        for rp in range(len(s2)):    
            if s2[rp] in s2Count:
                s2Count[s2[rp]] += 1
            else: 
                s2Count[s2[rp]] = 1
            
            if rp - lp + 1 == validSize:
                if s2Count == s1Count:
                    return True
                else:
                    s2Count[s2[lp]] -= 1
                    if s2Count[s2[lp]] == 0:
                        del s2Count[s2[lp]]
                    lp += 1

     
        return False
