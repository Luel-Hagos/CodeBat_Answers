def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)
def fix_teen(n):
  list1=[13,14,17,18,19]
  if  not n in list1:
    return n
  return 0
  