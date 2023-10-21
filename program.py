def main():
    x = input("Podaj wiek: ")
    try:
        if(int(x)>=18 and int(x)<=120):
            print("Użytkownik jest pełnoletni.")
        else:
            exit("Użytkownik jest niepełnoletni i/lub zbyt stary")
    except ValueError:
        print("Błedna wartość.")

def podaj_wiek():
    while True:
        wiek=input("Podaj wiek: ")
        if wiek.isdigit():
            return wiek
podaj_wiek()

def podajPlec():
    plec=""
    while plec != "M" and plec != "F":
        x = input("Podaj płeć: M - mężczyzna, F - kobieta: ")
        plec = x.upper()
    return plec

podajPlec()