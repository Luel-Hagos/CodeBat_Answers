def max_end3(nums):
  k=max(nums[0],nums[-1])
  for i in range(len(nums)):
    nums[i]=k
  return nums
