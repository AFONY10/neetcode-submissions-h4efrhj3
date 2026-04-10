class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary of group as key, and strings as values
        groupStrings = {}

        # For each string (s) in strings (strs):
        for s in strs:
            # Create groupName by sorting string (s)
            groupName = ''.join(sorted(s))

            # call setdefault() method from dictionary, paramters are keyName and default value which is empty list 
            # (if key-value pair are not yet created) and then just append values to list. 
            groupStrings.setdefault(groupName, []).append(s)
            
        return list(groupStrings.values())