while True:
    try:
        z = input("Podaj dzialanie + - * / ")
        a = float(input("Podaj liczbe a: "))
        b = float(input("Podaj liczbe b: "))
        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik dodawania {a} - {b} = {a - b}")
            case "*":
                print(f"Wynik dodawania {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik dodawania {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")
    except ValueError:
        print("Blad wartosci")
    else:
        print("Gdy nie ma bledu")
    finally:
        print("Zawsze")
        
