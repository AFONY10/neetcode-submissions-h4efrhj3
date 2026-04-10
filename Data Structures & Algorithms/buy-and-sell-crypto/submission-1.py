class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        mostProfit = 0
        leftPointer = 0
        rightPointer = leftPointer + 1
        n = len(prices)

        while rightPointer < n:
            currentBuy = prices[leftPointer]
            currentSell = prices[rightPointer]
             
            currentProfit = currentSell - currentBuy
            print("Current profit:", currentProfit)

            if currentSell < currentBuy:
                print(currentBuy, currentSell)
                leftPointer = rightPointer
                rightPointer += 1
                print("Values of L and R after moving window:", leftPointer, rightPointer)
                continue

            if currentProfit > mostProfit:
                mostProfit = currentProfit

            rightPointer += 1
        
        return mostProfit

