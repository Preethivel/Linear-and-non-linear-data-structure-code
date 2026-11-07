class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        l=0
        p=1
        cnt=0
        for r in range(len(nums)):
            p=p*nums[r]
            while p>=k and l<=r:
                p//=nums[l]
                l+=1
            cnt+=r-l+1
        return cnt
        
        
