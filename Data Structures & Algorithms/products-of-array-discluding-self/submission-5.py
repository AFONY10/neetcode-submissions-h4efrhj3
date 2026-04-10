class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodExSlf = []

        for i, n in enumerate(nums):
            currentProd = 1
            
            for j, num in enumerate(nums):
                if i == j:
                    continue
                else:
                    currentProd *= num

            prodExSlf.append(currentProd)
        
        return prodExSlf
            

