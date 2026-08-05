from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for string in strs:
            s = "".join(sorted(string))
            if s not in maps:
                maps[s] = [string]
            else:
                maps[s].append(string)
        return list(maps.values())