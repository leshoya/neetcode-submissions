class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            seen[val] = i
        for i,val in enumerate(nums):
            diff = target - val
            if diff in seen and seen[diff] != i:
                return [i, seen[diff]]
        
        return []