from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorteddict = defaultdict(list)
        for word in strs:
            alphabetical = ''.join(sorted(word))
            sorteddict[alphabetical].append(word)

        return list(sorteddict.values())
            
            
        