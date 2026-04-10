class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            # Append numbers
            if token not in operators:
                stack.append(int(token))
            
            # Given structure of RPN, there are at most 2 values in Stack before operator appears in string
            else:
                # Right = last inserted, left = first inserted
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))

        return stack[0]