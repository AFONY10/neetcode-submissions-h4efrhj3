class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupToString = defaultdict(list)
        res = []
        for s in strs:
            group = ''.join(sorted(s))
            groupToString[group].append(s)
        
        for values in groupToString.values():
            res.append(values)
        
        return res