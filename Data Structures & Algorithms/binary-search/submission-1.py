class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        ctr = 0 
        while l <= r:
            # if ctr == 3:
            #     return 0
            m = (l+r)//2

            # print(l, m, r)

            if nums[m] < target:
                l = m+1
            elif nums[m] > target: # target less middle.. go left
                r = m-1
            else:
                return m
            ctr+=1


        return -1
