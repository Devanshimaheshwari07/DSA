class Solution(object):
    def singleNonDuplicate(self, nums):
        ans=0
        for num in nums:
            ans=num^ans
        return ans
        