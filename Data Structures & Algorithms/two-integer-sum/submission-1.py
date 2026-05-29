class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}
        comp = 0
        for i, x in enumerate(nums):
            comp = target - x
            if comp in hash:
                return [hash[comp],i] 
            
            hash[x] = i






























        # map = {}

        # for i , num in enumerate(nums):
        #     diff = target - num

        #     if diff in map:
        #         return [map[diff], i]
            
        #     map[num] = i
            
