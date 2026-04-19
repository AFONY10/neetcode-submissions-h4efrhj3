class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        res = len(temperatures) * [0]

        for i in range(len(temperatures)-1, -1, -1):
            currentTemp = (temperatures[i], i)
            
            while tempStack and currentTemp[0] >= tempStack[-1][0]:
                tempStack.pop()
            
            if not tempStack:
                tempStack.append(currentTemp)
                continue
            else:
                res[i] = tempStack[-1][1] - currentTemp[1]
                tempStack.append(currentTemp)
    
        print(res)


        return res