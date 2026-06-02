class Solution:
        def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
                res = []

                def backtrack(i, path, numSum):
                        
                        if numSum == target:
                                print(numSum)
                                res.append(path.copy())
                                return
                        
                        if i >= len(nums) or numSum > target:
                                return
                        
                        currNum = nums[i]
                     
                        # try all posibilites with curr
                        path.append(currNum)
                        backtrack(i, path, numSum+currNum)
                        popped = path.pop()
                        

                        # Move onto next
                        backtrack(i+1, path, numSum)
                
                backtrack(0, [], 0)

                return res



