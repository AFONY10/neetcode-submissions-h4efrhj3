class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Initialize an empty hash_map (dictionary)
        hash_map = {}

        # Count occurrences of characters in string t
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        # Reduce the count based on occurrences in string s
        for c in s:
            if c not in hash_map or hash_map[c] == 0:
                return False
            hash_map[c] -= 1
        
        return True
