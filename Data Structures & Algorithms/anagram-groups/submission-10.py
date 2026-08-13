class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupToString = {}
        res = []
        for s in strs:
            group = ''.join(sorted(s))
            if group in groupToString:
                groupToString[group].append(s)
            else:
                groupToString[group] = [s]
        
        for values in groupToString.values():
            res.append(values)
        
        return res