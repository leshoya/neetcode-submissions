from collections import deque 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        queue = deque()

        for i, c in enumerate(s):
            counts[c] = counts.get(c, 0) + 1
            queue.append(i)
            while queue and counts[s[queue[0]]] > 1:
                queue.popleft()
        return queue[0] if queue else -1
        