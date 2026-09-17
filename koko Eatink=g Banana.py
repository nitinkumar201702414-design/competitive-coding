class Solution(object):
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)
        answer = right

        while left <= right:

            mid = (left + right) // 2
            totalHours = 0
            speed = mid

            for pile in piles:
                hours = (pile + speed - 1) // speed
                totalHours += hours

            if totalHours <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer