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
            
            # If current char is in tCount and the values of that key in both maps are same, 
            # then we can claim the character as one we "have"
            if s[rp] in tCount and sCount[s[rp]] == tCount[s[rp]]:
                have += 1
            
            # If and while we have all the chars we need
            while have == need:
                # Store result and update length for comparisons
                if rp - lp + 1 < resLen:
                    res = [lp, rp]
                    resLen = rp - lp + 1
                
                # Shrinking window: If lp-char in tCount and key value in sCount less than tCount,
                # we lost possesion of the char and we dont have it anymore
                sCount[s[lp]] -= 1
                if s[lp] in tCount and sCount[s[lp]] < tCount[s[lp]]:
                    have -= 1
                
                lp += 1
        
        # Initialize left and right index to strip string in [left:right] interval
        left = res[0]
        right = res[1]
        
        return s[left:right+1] if resLen != float('inf') else ""



