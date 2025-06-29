
kurierzy = ["DPD", "Fedex", "GLS"]

produkty = [
    "Myszka komputerowa(ergonomiczna)",
    "Laptop Asus Zenbook",
    "iPhone 14 Pro",
    "Monitor Acer Nitro",
    "Słuchawki bezprzewodowe JBL Tune 720BT",
    "Smartwatch Huawei Watch Fit 4 biały",
    "Ładowarka indukcyjna Apple MagSafe",
]

print("Dostępne produkty: ")


for i, produkt in enumerate(produkty): # numeracja produktów z listy
    print(f"{i + 1}. {produkt}")


wybrany_produkt = None


while wybrany_produkt == None: # pętla while aby zadawała pytanie dopóki nie padnie poprawny wybór 

    try:

        wybor = int(input("Wybierz numer produktu, który chcesz kupić: "))
        wybor = wybor - 1 # w pythonie liczymy od zera - przesunięcie żeby poprawić kolejność

        if 0 <= wybor < len(produkty):
            wybrany_produkt = produkty[wybor] # w tym miejscu ustalamy co to za produkt
            print("Wybrałeś: ", wybrany_produkt)
        else:
            print("Nieprawidłowy numer. Proszę wybrać numer z listy.")

    except ValueError:
        print("To nie jest prawidłowy numer. Proszę wpisać cyfrę.")


print("Dostępni kurierzy: ")


for k, kurier in enumerate(kurierzy):
    print(f"{k+1}. {kurier}")

wybrany_kurier = None

while wybrany_kurier == None:

    try:
        wybor2 = int(input("Wybierz dostawcę, który wręczy Twoje zamówienie: "))
        wybor2 = wybor2 -1 

        if 0 <= wybor2 < len(kurierzy):
            wybrany_kurier = kurierzy[wybor2]
            print("Wybrałeś dostawcę: ", wybrany_kurier)

        else:
            print("Nieprawidłowy numer. Proszę wybrać numer z listy.")

    except ValueError:
        print("To nie jest prawidłowy numer. Proszę wpisać cyfrę.")
    
print("Dziękujemy za złożenie zamówienia! Zabieramy się za jego szybką realizację!")






