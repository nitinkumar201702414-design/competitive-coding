class Solution:
	def arraySum(self, arr, n=0):
   		# code here
		if n == len(arr):
			return 0
		return self.arraySum(arr,n+1) + arr[n]

result=Solution()
print(result.arraySum([1,2,3,4]))