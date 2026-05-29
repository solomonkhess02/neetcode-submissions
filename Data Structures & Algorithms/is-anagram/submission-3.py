class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        for i, x in enumerate(s):
            dict_s[x] = i 
        
        for i, x in enumerate(t):
            dict_t[x] = i 

        if dict_t == dict_s:
            return True
        
        else:
            False





















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