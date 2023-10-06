# krotka(tupla)
tupla = "agata",
print(type(tupla))
print(tupla )
temp = 37,5
print(type(temp))
print((temp))
tupla2 = "Tomek", "Radek", "Zenek", "Marek"

print(type(tupla2))

tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))

print(tupla2.index("Tomek"))
print(tupla2.count("Tomek"))

a, b = 1, 2
print(a)
print(b)
print(type((1,2)))

a, *b = 1, 2, 3
print(a)
print(b)

print(tupla2)
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)

lista = list(tupla3)
print(lista)
print(type(lista))

