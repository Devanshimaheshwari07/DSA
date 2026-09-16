class Solution(object):
    def myPow(self, x, n):
        if n==0:
            return 1
        else:
            return x*x**(n-1)


       