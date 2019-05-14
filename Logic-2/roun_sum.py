def round_sum(a, b, c):
  sum=0
  sum+=round10(a)
  sum+=round10(b)
  sum+=round10(c)
  return sum

def round10(num):
  k=num%10
  l=10-num%10
  if num%10>=5:
    return num+l
  return  num-k
  
