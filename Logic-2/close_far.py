def close_far(a, b, c):
  if a>=b and a>=c:
    if abs(c-b)<=1:
      return False
    else:
      return True
  elif abs(a-b)<=1:
    if  abs(a-c)>=2 and abs(b-c)>=2:
      return True
    else:
      return False
  elif abs(a-c)<=1:
    if  abs(a-b)>=2 and abs(c-b)>=2:
      return True
    else:
      return False
