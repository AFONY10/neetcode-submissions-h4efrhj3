class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict where each value is initialized as an empty list
        res = defaultdict(list)
        
        for s in strs:
            # Sort the string to get a standardized "anagram key"
            # For example, "eat", "tea", and "ate" will all become "aet"
            sortedS = ''.join(sorted(s))
            
            # Group the original string under the sorted key
            res[sortedS].append(s)  # defaultdict will initialize the key if not already exisiting. 
                                    # If regular dictionary was used, you would have to use setdefault(sortedS,[]).append(s)
        
        # Return all grouped anagrams as a list of lists
        return list(res.values())
