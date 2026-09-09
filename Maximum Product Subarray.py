class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMax = nums[0]
        currentMin = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            oldMax = currentMax

            currentMax = max(num, oldMax * num, currentMin * num)
            currentMin = min(num, oldMax * num, currentMin * num)

            answer = max(answer, currentMax)

        return answer