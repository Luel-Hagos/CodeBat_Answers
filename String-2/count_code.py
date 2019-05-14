def count_code(str):
  sum=0
  for i in range(len(str)-3):
    if(str[i]=='c'and str[i+1]=='o' and str[i+3]=='e'):
      sum+=1
  return sum
