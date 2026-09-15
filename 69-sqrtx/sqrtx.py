class Solution(object):
    def mySqrt(self, x):
        l=0
        h=x
        valid=0
        while l<=h:
            mid=(l+h)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                h=mid-1
                
            elif mid*mid<x:
                valid=mid
                l=mid+1
                
        return valid 



        