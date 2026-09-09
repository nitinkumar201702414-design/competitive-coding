class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, n in enumerate(nums):
            x = target - n

            if x in d:
                return [d[x], i]

            d[n] = i

            # TC = O(n)

#---------------------------------------------------------------------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == traget:
                    return[i,j]
                
                # TC = O(n^2)

