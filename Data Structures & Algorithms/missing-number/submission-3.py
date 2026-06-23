class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # hash = set(nums)

        # for x in range(len(nums)+1):
        #     if x not in hash:
        #         return x

        n = len(nums)
        expected_sum = (n*(n+1))/2
        actual_sum = sum(nums)

        x = expected_sum-actual_sum
        return int(round(x))
