from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        ordered = sorted(counts.items(), key=lambda item:item[1], reverse=True)
        return [num for num, freq in ordered[:k]]


        

