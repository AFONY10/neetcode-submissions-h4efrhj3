# 1. Hashmap to groupAnagrams (string, list)
# 2. Append values of hash keys into a return array
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpList = {}
        output = []
        n = len(strs)

        # Creating Hashmap to groupAnagrams
        for i in range(n):
            key = ''.join(sorted(strs[i]))
            if key not in grpList:
                grpList[key] = [strs[i]]
            else:
                grpList[key].append(strs[i])
                
        # Append values of hashmap to output list
        for key in grpList:
            output.append(grpList[key])
        
        return output


