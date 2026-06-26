class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            long = 0
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                long += 1
            longest = max(longest, long)
        return longest

        
        # strset = set()
        # l, r = 0, len(str) - 1
        # while l<r:
        #     if 



