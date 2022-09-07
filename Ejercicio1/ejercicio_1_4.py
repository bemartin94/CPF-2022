mesa= ["A_S", "J_H", "7_D", "8_D", "10_D"]
mano= ["J_D", "3_D"]

def contar_cartas(palo):
  mesa_string = ' '.join(mesa)
  mano_string = ' '.join(mano)
  total= mesa_string.count(palo) + mano_string.count(palo)
  return total


def check_flush(mesa, mano):
  if contar_cartas("D") >= 5:
      return True, "// diamantes"
  if contar_cartas("S") >= 5:
      return True, "// espadas"
  if contar_cartas("C") >= 5:
      return True, "// tréboles"
  if contar_cartas("H") >= 5:
      return True, "// corazones"

check_flush(mesa, mano)