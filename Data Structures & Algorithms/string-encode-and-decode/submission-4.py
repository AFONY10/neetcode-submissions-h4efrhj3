class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wordSize = int(s[i:j])
            res.append(s[j+1 : j+1+wordSize])
            i = j+1+wordSize
        return res

