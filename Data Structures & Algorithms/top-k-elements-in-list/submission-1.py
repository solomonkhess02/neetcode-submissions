class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        for x in nums:
            count[x] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result


        # hash = defaultdict(int)
        # for x in nums:
        #     hash[x] += 1
        
        # sorted_list = sorted(hash.keys(), key = hash.get, reverse = True)
        # return sorted_list[:k]
