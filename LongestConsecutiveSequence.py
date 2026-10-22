def LongestConsecutiveSequence(nums):
  s=set(nums)
  res=0
  for n in s:
    if n-1 not in s:
      l=1
      while n+l in s:
        l+=1
    res=max(res,l)
  return res
