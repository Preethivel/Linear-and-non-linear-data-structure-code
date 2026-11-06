from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        ws=sum(nums[0:k])
        seen=defaultdict(int)
        
        for i in range(k):
            seen[nums[i]]+=1
        m=ws if len(seen)==k else 0
        l=0
        for r in range(k,len(nums)):
            seen[nums[r]]+=1
            ws+=nums[r]
            seen[nums[l]]-=1
            if seen[nums[l]]==0:
                del seen[nums[l]]
            ws-=nums[l]
            l+=1
            if len(seen)==k:
                m=max(m,ws)
        return m
