from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        top_k = counts.most_common(k) #[(num, freq,..)]
        return [num for num, freq in top_k]
        


        

 