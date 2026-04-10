class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_s = ""

        for s in strs:
            encoded_s += str(len(s)) + "#" + s
        
        print(encoded_s)
        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        # Pointer to start of encoded string 
        # which updates as the inner while loop finds the lenghts of each of the encoded strings
        while i < len(s):
            j = i
            # Single out the length of string
            while s[j] != '#':
                j += 1
            currentWordLength = int(s[i:j])
            decoded_strs.append(s[j+1 : j+1+currentWordLength])
            print(currentWordLength)
            i = j + 1 + currentWordLength

        return decoded_strs
