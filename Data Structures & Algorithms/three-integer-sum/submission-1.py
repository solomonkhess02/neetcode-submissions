class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
        nums.sort()
        
        res = []
        for i, a in enumerate(nums):
            if a == nums[i-1] and i > 0:
                continue
            
            l,r = i + 1, len(nums)-1

            while l<r:
                if (a + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (a + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res


    
    
        # nums.sort()
        # result = set()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 result.add((nums[i],nums[j],nums[k]))
        
        # return [list(triplet) for triplet in result]