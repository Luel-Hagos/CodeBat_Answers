def cigar_party(cigars, is_weekend):
  if is_weekend:
    if cigars>60:
      return True
    elif 40<=cigars<=60:
      return True
    return False
  elif not is_weekend and cigars<40 or cigars>60:
    return False
  else:
    return True
  
