class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen={}

        for i in range(len(nums)):
            if nums[i] in last_seen:
                dist=i-last_seen[nums[i]]
                if dist<=k:
                    return True

            last_seen[nums[i]]=i
                

        return False
        