class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        m=float('inf')
        l=0
        s=0
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                m=min(m,r-l+1)
                s-=nums[l]
                l+=1
        return 0 if m==float('inf') else m
        


        
