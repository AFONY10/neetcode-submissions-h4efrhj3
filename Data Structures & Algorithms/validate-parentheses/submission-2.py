class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')':'(', ']':'[', '}':'{'}

        for i, bracket in enumerate(s):
            if bracket not in closeToOpen:
                stack.append(bracket)
            else:
                if stack and closeToOpen[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack: 
            return True 
        else:  
            return False
