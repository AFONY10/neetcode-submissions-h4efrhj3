class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = {}
        sCount = {}
        # Build frequency map for all chars in t
        for c in t:
            if c in tCount:
                tCount[c] += 1
            else:
                tCount[c] = 1
        print(tCount, len(tCount))

        lp = 0
        res = [-1, -1]
        resLen = float('inf')
        have, need = 0, len(tCount)
        for rp in range(len(s)):
            # Append key and value to sCount
            if s[rp] in sCount:
                sCount[s[rp]] += 1
            else:
                sCount[s[rp]] = 1
            
            # If current c is in tCount and 
            if s[rp] in tCount and sCount[s[rp]] == tCount[s[rp]]:
                have += 1
            
            while have == need:
                if rp - lp + 1 < resLen:
                    res = [lp, rp]
                    resLen = rp - lp + 1

                sCount[s[lp]] -= 1
               
                if s[lp] in tCount and sCount[s[lp]] < tCount[s[lp]]:
                    have -= 1
                
                lp += 1
            
        lp = res[0]
        rp = res[1]
        
        return s[lp:rp+1] if resLen != float('inf') else ""



