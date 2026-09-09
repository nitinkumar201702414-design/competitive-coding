class Solution:
    def factorial(self, n: int) -> int:
        # code here
        
        #   Recursion
        
        # if n <=1:
        #     return 1
        # return n * self.factorial(n-1)
        
        #   Iteration
        
        result = 1
        for i in range(1,n+1):
            result*=i
        return result

result=Solution()
print(result.factorial(5))