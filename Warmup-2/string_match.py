def string_match(a, b):
  if len(a)>len(b):
    length=len(b)
  else:
    length=len(a)
  counter=0
  for i in range(length-1):
    k=a[i]+a[i+1]
    l=b[i]+b[i+1]
    if k==l:
      counter+=1
  return counter
