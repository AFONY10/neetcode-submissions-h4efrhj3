class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) != len(speed):
            return 0
        time = 0
        posSpeed = []

        # Compute array with combined indices
        for i, pos in enumerate(position):
            posSpeed.append((pos,speed[i]))
        
        # Sort array based on position
        posSpeed.sort(key=lambda x: x[0])
        print(posSpeed)

        stack = []
        for i in range(len(posSpeed)-1, -1, -1):
            currentTime = (target-posSpeed[i][0])/posSpeed[i][1]
            if stack and stack[-1][1] >= currentTime:
                continue
            else:
                stack.append((posSpeed[i],currentTime))
            print(stack)
        

        fleets = len(stack)
        return fleets



        