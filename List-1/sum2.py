def sum2(nums):
  k=len(nums)
  sum=0
  if k==0:
    sum=0
  elif k<=2:
    for i in range(k):
      sum+=nums[i]
  else:
      sum=nums[0]+nums[1]
  return sum
