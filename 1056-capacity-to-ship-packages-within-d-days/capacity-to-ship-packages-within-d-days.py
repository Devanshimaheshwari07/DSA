class Solution(object):
    def shipWithinDays(self, weights, days):
        l=max(weights)
        h=sum(weights)
        
        while l<h:
            current_day=0
            days_taken=1
            mid=(l+h)//2
            for weight in weights:
                if current_day+weight<=mid:
                    current_day+=weight
                else:
                    days_taken+=1
                    current_day=weight

            if days_taken<=days:
                h=mid
            else:
                l=mid+1

        return l