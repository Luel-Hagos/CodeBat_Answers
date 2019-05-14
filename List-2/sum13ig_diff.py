def sum13(nums):
  sum=0
  i=0
  length=len(nums)
  if length==0:
    return 0
  while i<length:
    if nums[i]==13:
      i+=2
      continue 
    sum+=nums[i]
    i+=1
  return sum