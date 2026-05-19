class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # result = [x * y for x, y in zip(nums, nums)]
        # result.sort()
        # return result

        l, r = 0, len(nums)-1
        res = []

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l]*nums[l])
                l += 1
            
            else:
                res.append(nums[r]*nums[r])
                r -= 1
        
        return res[::-1]


                