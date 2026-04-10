class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            
            while temperatures[i] >= stack[-1][0]:
                stack.pop()
                if not stack:
                    stack.append((temperatures[i], i))
                    break
            
            res[i] = stack[-1][1] - i
            print(res[i])
            stack.append((temperatures[i], i))

            
        return res
