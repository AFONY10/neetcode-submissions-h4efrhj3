class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        # Define res to store string array/List
        res = []
        # Define index to keep track of where we are at the encoded string
        i = 0

        # While our tracker is in the encoded string
        while i < len(s):
            j = i # new tracker to look for delimiter
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # from i to j in the encoded string, we find the number in string-format, which then becomes an integer
            res.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        return res


