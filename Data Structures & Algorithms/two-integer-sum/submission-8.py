class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary/Hash map to store num keys and index as values
        numIndex = {}

        # Iterting for all index (i) and their values (v) in the enumerate nums list
        for i, v in enumerate(nums):
            # Find complement value
            complement = target - v

            # If complement is in dictionary
            if complement in numIndex:
                return [numIndex[complement], i]
                # Complement index returned first since it's the first stored index in dictionary.
            # Store in index, to be called first since dictionary is empty. 
            # If-statement can't be invoked beofre there's enough in th enough values in dictionary
            numIndex[v] = i
        
        return []


        