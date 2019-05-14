def extra_end(str):
  leng=len(str)
  if leng<=2:
    return str*3
  return str[leng-2:]*3
