#Prefix And Sufix Method
#TimeComplixity = O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        leftMax = [0]*n
        rightMax = [0]*n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        water = 0
        for i in range(n):
            water += min(leftMax[i],rightMax[i])- height[i]
        return water

#------------------------------------------------------------------
#Two Pointer Technique
#TimeComplixity = O()

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0
        water = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]

                left += 1

            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]

                right -= 1

        return water