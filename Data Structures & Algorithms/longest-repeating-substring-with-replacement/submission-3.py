class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        lp = 0
        maxLength = 0
        maxFreq = 0

        for rp in range(len(s)):
            # Focusing on building the hashmap
            if s[rp] in charCount:
                charCount[s[rp]] += 1
            else:
                charCount[s[rp]] = 1
            
            # Update maxFreq in valid window
            if charCount[s[rp]] > maxFreq:
                maxFreq = charCount[s[rp]]
            
            # If window is invalid, move lp up
            while (rp - lp + 1) - maxFreq > k:
                charCount[s[lp]] -= 1
                lp += 1
            
            # Record lenghts
            currentLength = rp - lp + 1
            if currentLength > maxLength:
                maxLength = currentLength

        return maxLength