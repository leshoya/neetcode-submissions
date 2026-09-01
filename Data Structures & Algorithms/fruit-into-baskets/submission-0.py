from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        counts = defaultdict(int)
        answer = 0

        for right in range(len(fruits)):
            counts[fruits[right]] += 1

            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1

            answer = max(answer, right - left + 1)

        return answer
