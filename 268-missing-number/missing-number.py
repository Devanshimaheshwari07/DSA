class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        exp=(n*(n+1))/2
        act=0

        for i in range(n):
            act+=nums[i]

        num=exp-act
        return num
        

        