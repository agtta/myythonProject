tekst = "Witaj swiecie"
print(tekst)
print(type(tekst))  # <c;ass str>

tekst2 = tekst.upper()
print(tekst)
print(tekst2)

print(tekst[0])
print(len(tekst))

imie = 'Agata'
tekst_format = f"Mam na imie {imie} i lubie Pythona"
print(tekst_format)

starszy = "Witaj %s"
print(starszy % imie)