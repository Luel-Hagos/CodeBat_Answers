def centered_average(nums):
  sum=0
  small=min(nums)
  large=max(nums)
  length=len(nums)
  for i in nums:
    sum+=i
  return (sum-large-small)/(length-2)
