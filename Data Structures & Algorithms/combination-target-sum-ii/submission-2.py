class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, path, numSum):
            if numSum == target:
                res.append(path.copy())
                return
            if i >= len(candidates) or numSum > target:
                return

            currNum = candidates[i]
            
            # Include
            path.append(currNum)
            backtrack(i + 1, path, numSum + currNum)
            path.pop()

            # Exclude / Skip
            while i < len(candidates) -1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, path, numSum)

        backtrack(0, [], 0)

        return res