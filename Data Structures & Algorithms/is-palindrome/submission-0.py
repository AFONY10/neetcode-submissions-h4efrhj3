class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        leftP = 0
        rightP = len(newStr) - 1

        while leftP < rightP:
            if newStr[leftP] != newStr[rightP]:
                print(newStr[leftP])
                print(newStr[rightP])
                return False
            leftP += 1
            rightP -= 1
        
        return True
        