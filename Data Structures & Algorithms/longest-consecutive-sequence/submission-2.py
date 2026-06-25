class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        numset = set(nums)
        for n in numset:
            if (n-1) not in numset:
                length = 0
                while (n+length) in numset:
                    length +=1
            
                longest = max(length, longest)
        return longest    



        # count = 1
        # max_count = 0
        # nums.sort()
        # for i in range(0, len(nums)):
        #     target = nums[i]+1
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == nums[j-1] and j>i+1:
        #             continue
        #         if nums[j] == target:
        #             count+=1
        #             target+=1
        #     max_count = max(count, max_count)
        #     count = 1
        # return max_count