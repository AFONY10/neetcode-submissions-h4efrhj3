class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make new string that is solely alphenumeric chracters and in lowercase
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        # Two pointers
        leftP = 0
        rightP = len(newStr) - 1

        # The two pointers are moving towards each other while they are different values
        while leftP < rightP:
            if newStr[leftP] != newStr[rightP]:
                return False
            leftP += 1
            rightP -= 1
        
        return True
        