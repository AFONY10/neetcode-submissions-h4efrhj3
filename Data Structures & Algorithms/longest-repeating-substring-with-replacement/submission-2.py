
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        lp = 0
        maxLength = 0
        maxFreq = 0

        for rp in range(len(s)):
            charCount[s[rp]] = charCount.get(s[rp], 0) + 1
            maxFreq = max(maxFreq, charCount[s[rp]])

            while (rp - lp + 1) - maxFreq > k:
                charCount[s[lp]] -= 1
                lp += 1

            maxLength = max(maxLength, rp - lp + 1)

        return maxLength