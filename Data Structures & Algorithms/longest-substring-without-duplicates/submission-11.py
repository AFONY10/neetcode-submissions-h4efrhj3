class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1

        maxLength = 0
        distinctChars = set()

        lp = 0
        rp = lp
        # Two Pointer approach: Expand window if window valid
        while rp < len(s):
            currentLength = rp-lp + 1

            # If window is not valid, shrink it from the left
            if s[rp] in distinctChars:
                # Shrink window till duplicate pos is found
                while s[lp] != s[rp]:
                    distinctChars.remove(s[lp])
                    lp += 1
                # Removing duplicate itself and incrementing to next valid
                distinctChars.remove(s[lp])
                lp += 1
                continue

            # Expanding window with valid chars
            distinctChars.add(s[rp])
            if currentLength > maxLength:
                    maxLength = currentLength
            rp += 1


        
        return maxLength