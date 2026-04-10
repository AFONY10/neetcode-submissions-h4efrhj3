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

        while rp < len(s):
            currentLength = rp-lp + 1
            if s[rp] in distinctChars:
                if currentLength > maxLength:
                    maxLength = currentLength - 1
                while s[lp] != s[rp]:
                    distinctChars.remove(s[lp])
                    lp += 1
                distinctChars.remove(s[lp])
                lp += 1

                
                continue

            distinctChars.add(s[rp])
            if currentLength > maxLength:
                    maxLength = currentLength
            rp += 1


        
        return maxLength