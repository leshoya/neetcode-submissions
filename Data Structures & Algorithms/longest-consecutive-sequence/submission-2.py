from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if n - 1 in numset:
                continue
            length = 1
            curr = n
            while curr + 1 in numset:
                curr += 1
                length += 1
            longest = max(longest, length)

        
        return longest
        



        