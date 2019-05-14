def string_bits(str):
  result=""
  length=len(str)
  for i in range(length):
    if i % 2 == 0:
      result = result + str[i]
  return result
    
