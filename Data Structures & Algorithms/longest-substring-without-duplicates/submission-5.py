class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) < 2:
            return 1

        maxLength = 0
        distinctChars = set()
        

        for i, c in enumerate(s):
            distinctChars.add(c)

            for j in range(i+1,len(s)):
                if s[j] in distinctChars:
                    break

                distinctChars.add(s[j])
                
            currentLength = len(distinctChars)
            if currentLength > maxLength:
                    maxLength = currentLength
            distinctChars.clear()

        
        return maxLength