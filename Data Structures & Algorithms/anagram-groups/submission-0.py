class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for x in strs:
            sorted_word = "".join(sorted(x))
        
            if sorted_word not in hash:
                hash[sorted_word] = []
            
            hash[sorted_word].append(x)

        return list(hash.values())


