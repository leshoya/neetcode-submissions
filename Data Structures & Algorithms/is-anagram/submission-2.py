class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seena = {}
        seenb = {}
        for i in range(len(s)):
            if s[i] not in seena:
                seena[s[i]] = 1
            if t[i] not in seenb:
                seenb[t[i]] = 1
            seena[s[i]] += 1
            seenb[t[i]] += 1
        
        return seena == seenb



        