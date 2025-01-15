from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = defaultdict(int)
        
        for num in nums:
            if num in num_map.keys():
                num_map[num] += 1
            else:
                num_map[num] = 1
        sorted_num_map = dict(sorted(num_map.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_num_map.keys())[:k]
