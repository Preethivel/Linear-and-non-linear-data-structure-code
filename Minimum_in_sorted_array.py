def findMin(nums):

 1, r=0, len(nums)-1

 while 1 < r:

  mid = (1+r)//2

  if nums [mid] > nums[r]: 1 = mid+1

  else:

  r = mid

 return nums [1]
