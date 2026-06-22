class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        known = set()
        for n in nums:
            if n in known:
                return True
            known.add(n)
        return False