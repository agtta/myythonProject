dictionary = {}
print(dictionary)

dictionary['imie'] = 'Radek'
print(dictionary)
dictionary['wiek'] = 39
print(dictionary)

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 5)])
print(dictionary1)
print(dictionary1['x'])

dict2 = {'imie' : 'name', 'kot' : 'cat', 'pies' : 'dog'}
print(dict2['imie'])

print('Mam w slowniku', dict2.keys())
key = input("Podaj slowko do przetlumaczenia: ")
print(dict2[key])
print(dict2[key.replace(" ", "").lower()])

# kalkulator
a = int(input("Podaj pierwsza liczbe"))
# b = float(input("Podaj druga liczbe"))
b = (input("Podaj druga liczbe"))
print(type(a))
print(a + int(b))

