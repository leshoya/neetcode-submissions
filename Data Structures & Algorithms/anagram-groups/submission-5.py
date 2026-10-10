from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        res = []
        for s in strs:
            group["".join(sorted(s))].append(s)
        for val in group.values():
            res.append(val)
        return res