import random
for i in range(10):
    print(i)

for i in range(10):
    pass

for _ in range(10):
    pass

lista2 = list(range(1, 50))
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)
    