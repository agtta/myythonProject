while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnozenie
    4. Dzielenie
    5. Koniec""")

    odp = input("Podaj operacje")
    if odp == '5':
        break
    try:
        a = float(input("Podaj pierwsza liczbe"))
        b = float(input("Podaj druga liczbe"))

        if odp == '1':
            print("Wynik", a +b )
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a * b)
        elif odp == '4':
            print("Wynik", a / b)
        else:
            print("nie znam takiego dzialania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Blad wartosci")
    except Exception as e:
        print("Blad", e)
    else:
        print("Gdy nie ma bledu")
    finally:
        print("Zawsze")
        

