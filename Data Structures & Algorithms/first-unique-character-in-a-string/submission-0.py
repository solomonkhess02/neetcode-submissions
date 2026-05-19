class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        map = {}

        for i in s:
            map[i] = map.get(i, 0) + 1
        
        for i , c in enumerate(s):
            if map[c] == 1:
                return i
        
        return -1