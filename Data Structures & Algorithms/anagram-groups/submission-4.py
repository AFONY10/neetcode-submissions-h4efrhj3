class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupStrings = {}

        for s in strs:
            groupName = ''.join(sorted(s))
            groupStrings.setdefault(groupName, []).append(s)
        return list(groupStrings.values())