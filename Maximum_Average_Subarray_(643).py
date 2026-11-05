def maximum_average_subarray(nums,k):
  m=float('-inf')
  s=sum(nums[0:k])
  for i in range(k,len(nums)-k+1):
    s=s-nums[i-1]+nums[i+k-1]
    m=max(m,s/k)
  return m
    
