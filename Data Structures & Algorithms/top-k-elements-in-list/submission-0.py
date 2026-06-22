class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = 1 + res.get(num, 0) 
        
        sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)

        top = [item[0] for item in sorted_res[:k]]

        return top


        

