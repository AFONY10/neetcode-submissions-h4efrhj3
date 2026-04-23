class TimeMap:

    def __init__(self):
        self.name = "TimeMap"
        self.keyValue = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyValue:
            self.keyValue[key].append((timestamp,value))
        else:
            self.keyValue[key] = [(timestamp,value)]
        
        print(self.keyValue)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyValue:
            return ""

        res = ""
        values = self.keyValue[key]
        lp, rp = 0, len(values)-1

        while lp <= rp:
            mp = (rp+lp) // 2
            currentTime, currentVal = values[mp]

            if currentTime == timestamp:
                return currentVal
            elif currentTime < timestamp:
                res = currentVal
                lp = mp + 1
            else:
                rp = mp - 1

        return res
