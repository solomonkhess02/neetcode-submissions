class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hash = set(nums)

        for x in range(len(nums)+1):
            if x not in hash:
                return x

        # hash1, hash2 = {}, {}
        
        # for x in nums:

