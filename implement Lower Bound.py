class sloutin:
    def lowerBound(self,arr,traget):
        for index, value in enumerate(arr):
            if value >= traget:
                return index
            return(arr)
        
#Linear Search

#---------------------------------------------------------------


class Solution:
    def lowerBound(self, arr, target):
        n = len(arr)
        for i in range(0,n):
            if arr[i] >= target:
                return i
        return n

#----------------------------------------------------

#Binary Search

class Solution:
    def lowerBound(self, arr, target):
        # code here
        left , right , answer = 0, len(arr)-1, len(arr)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                answer = mid
                right = mid -1 
            else:
                left = mid -1
            return answer