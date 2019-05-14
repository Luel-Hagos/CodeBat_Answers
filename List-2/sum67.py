def sum67(nums):
  sum=0
  found=True
  for i in nums:
    if i==6:
      found=False
    if found:
      sum+=i
      continue
    if i==7:
      found=True
  return sum