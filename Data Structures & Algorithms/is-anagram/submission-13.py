class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early return if both strings are not same length
        if len(s) != len(t):
            return False

        # Declare Dictionary
        charCount = {}

        # Constructing charCount based off of string s
        for c in s:
            if c in charCount:
                charCount[c] += 1
            else:
                charCount[c] = 1


        # Destructing charCount based off of string t
        for c in t:
            if c not in charCount or charCount[c] == 0:
                return False
            else:
                charCount[c] -= 1
        return True


