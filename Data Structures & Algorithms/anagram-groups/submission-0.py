class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        
        for word in strs:
            sortedw = ''.join(sorted(word))
            group[sortedw].append(word)
        return list(group.values())
