from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_map = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))
        return list(freq_map.keys())[:k]