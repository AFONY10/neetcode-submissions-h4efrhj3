class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pos(x) and speed(v) stack and sort it
        xv = []
        for i in range(len(position)):
            xv.append((position[i],speed[i]))
        xv.sort(key=lambda xv: xv[0])
        print(xv)
        
        # Create stack
        fleets = []
        for car in range(len(xv)-1, -1, -1):
            currentCar = xv[car]
            currentTime = (target-currentCar[0])/currentCar[1]

            if fleets and currentTime <= fleets[-1][1]:
                continue
            else:
                fleets.append((currentCar, currentTime))
        
        return len(fleets)


