def last2(str):
  length=len(str)
  checker=""
  counter=0
  if length<2:
    return 0
  end=str[length-2:]
  for i in range(length-2):
    checker=str[i:i+2]
    if checker==end:
      counter+=1
  return counter