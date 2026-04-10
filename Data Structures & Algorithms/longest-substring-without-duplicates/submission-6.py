class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1

        maxLength = 0
        distinctChars = set()

        # Brute force: Let every chracter be beginning in substring
        for i, c in enumerate(s):
            distinctChars.add(c)

            # Append new chars in set until duplicate is seen.
            for j in range(i+1,len(s)):
                if s[j] in distinctChars:
                    break

                distinctChars.add(s[j])
            
            # Record length before duplicate was seen
            currentLength = len(distinctChars)
            if currentLength > maxLength:
                    maxLength = currentLength
            
            # Clear to start from scratch with a new start char
            distinctChars.clear()

        
        return maxLength