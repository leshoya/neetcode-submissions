class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sorteddict = {}
        for word in strs:
            alphabetical = ''.join(sorted(word))
            if alphabetical not in sorteddict:
                sorteddict[alphabetical] = [word]
            else:
                sorteddict[alphabetical].append(word)

        for key, v in sorteddict.items():
            result.append(v)
        return result