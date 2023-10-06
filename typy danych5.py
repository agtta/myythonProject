lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)
print(type(zbior))
zb2 = set()
print(zb2)

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)

zbior2 = {66, 11, 44, 18, 52, 999, 999}
print(zbior2)
print(zbior | zbior2)
print(zbior & zbior2)
print(zbior - zbior2)
print(zbior2 - zbior)
print(zbior.difference(zbior2))
print(zbior2.difference(zbior))
print(zbior)
print(zbior2)
