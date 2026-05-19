class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashs = {}
        hasht = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hashs[s[i]] = hashs.get(s[i], 0) + 1
            hasht[t[i]] = hasht.get(t[i], 0) + 1
        
        for c in hashs:
            if hashs[c] != hasht.get(c, 0):
                return False
        
        return True