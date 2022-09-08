def check_flush(mesa, mano):
  palos= ["D", "S", "H", "C"]
  total= []
  mesa_string = ' '.join(mesa)
  mano_string = ' '.join(mano)
  for item in palos:
    total.append(mesa_string.count(item) + mano_string.count(item))
  if any(item >= 5 for item in total):
    return True
  return False