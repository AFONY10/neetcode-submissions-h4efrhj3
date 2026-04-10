class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charDict = {}

        # Construct charDict
        for c in s:
            if c in charDict:
                charDict[c] += 1
            else:
                charDict[c] = 1
        
        # Destruct charDict
        for c in t:
            if c in charDict and charDict[c] > 0:
                charDict[c] -= 1
            else:
                return False
        
        return True