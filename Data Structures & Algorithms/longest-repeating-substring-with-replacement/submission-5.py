class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        n = len(s)
        charCount = {}
        longest = 0
        
        for rp in range(n):
            if s[rp] in charCount:
                charCount[s[rp]] += 1
            else:
                charCount[s[rp]] = 1
            
            
            while rp - lp + 1 - max(charCount.values()) > k:
                charCount[s[lp]] -= 1
                lp += 1
            
            length = rp - lp + 1
            if length > longest:
                longest = length
        return longest
            