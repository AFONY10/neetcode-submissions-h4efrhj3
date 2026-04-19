class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        tokenStack = []

        for c in tokens:
            if c not in operators:
                tokenStack.append(int(c))
            else:
                rightItem = tokenStack.pop()
                leftItem = tokenStack.pop()

                if c == '+':
                    tokenStack.append(leftItem + rightItem)
                elif c == '-':
                    tokenStack.append(leftItem - rightItem)
                elif c == '*':
                    tokenStack.append(leftItem * rightItem)
                elif c == '/':
                    tokenStack.append(int(leftItem / rightItem))

            print(tokenStack)
        return tokenStack[0]