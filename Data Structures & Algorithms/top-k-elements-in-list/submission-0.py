class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for x in nums:
            hash[x] += 1
        
        sorted_list = sorted(hash.keys(), key = hash.get, reverse = True)
        return sorted_list[:k]
