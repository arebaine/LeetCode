from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = sorted(list(counter.keys()), key=lambda x: -counter[x])
        return freq[:k]
