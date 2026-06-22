class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        hash = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in hash:
                return [hash[diff], i] 
            hash[nums[i]] = i
