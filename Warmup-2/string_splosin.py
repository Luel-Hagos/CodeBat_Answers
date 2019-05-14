def string_splosion(str):
  res=""
  for i in range(len(str)):
    for j in range(i+1):
      res+=str[j]
  return res
