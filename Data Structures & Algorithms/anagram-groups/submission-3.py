class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupStrings = defaultdict(list)

        for s in strs:
            groupName = ''.join(sorted(s))
            groupStrings[groupName].append(s)
        return list(groupStrings.values())