class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        left=[0]*n
        right=[0]*n
        left[0]=1
        right[n-1]=1

        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            right[j]=right[j+1]*nums[j+1]
        
        ans=[0]*n
        for i in range(0,n):
            ans[i]=left[i]*right[i]
        
        return ans

        


        