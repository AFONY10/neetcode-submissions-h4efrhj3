# 1. sort array: candidates = [1, 2, 2, 4, 5, 6, 9]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, path, numSum):
            if numSum == target:
                res.append(path.copy())
                return
            if numSum > target or i >= n:
                return
            
            currNum = candidates[i]
            numSum += currNum

            # Include subtree
            path.append(currNum)
            backtrack(i + 1, path, numSum)
            popped = path.pop()
            numSum -= popped

            # Exclude/Skip subtree
            while i + 1 < n and candidates[i] == candidates[i + 1]: # We return back to root of decisiontree. And so we want to skip duplicate combinations
                i += 1
            backtrack(i + 1, path, numSum)
        
        backtrack(0, [], 0)

        return res