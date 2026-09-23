lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto: uusi / haku / lopeta: ").lower()

    if toiminto == "uusi":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")

        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif toiminto == "haku":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()

        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")

    elif toiminto == "lopeta":
        break

    else:
        print("Tuntematon toiminto.")

    