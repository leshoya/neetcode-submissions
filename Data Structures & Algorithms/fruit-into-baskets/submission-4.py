from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        counts = defaultdict(int)
        res = 0

        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1

            res = max(res, r - left + 1)
            
        return res
