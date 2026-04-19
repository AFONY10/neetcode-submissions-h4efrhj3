class Solution:
    def isValid(self, s: str) -> bool:
        closeOpen = {']':'[', ')':'(', '}':'{'}
        stack = []

        for c in s:
            if c in closeOpen and len(stack) != 0:
                if stack[-1] == closeOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
            print(stack)
        
        if len(stack) == 0:
            return True
        else:
            return False