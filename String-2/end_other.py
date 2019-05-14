def end_other(a, b):
  k=len(a)
  kk=len(b)
  if k<kk:
    return a[0:].lower()==b[-k:].lower()
  else:
    return a[-kk:].lower()==b[0:].lower()
  
