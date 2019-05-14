def front_back(str):
  leng=len(str)
  if leng<=1:
    return str
  return str[leng-1]+str[1:leng-1]+str[0]