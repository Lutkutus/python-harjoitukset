import random

from pathlib import Path

kansio = Path(__file__).parent

class Esine:
    def __init__(self, nimi, paino, arvo=0):
        self.nimi = nimi
        self.paino = paino
        self.arvo = arvo


class Huone:
    def __init__(self, nimi, esine, kuva):
        self.nimi = nimi
        self.esine = esine
        self.kuva = kuva


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.reppu = []
        self.sijainti = sijainti

    def liiku(self, huone):
        self.sijainti = huone
        print(f"Menit paikkaan {huone.nimi}")
        print(huone.kuva)

    def keraa_esine(self):
        if self.sijainti.esine != None:
            self.reppu.append(self.sijainti.esine)
            print(f"Löysit esineen {self.sijainti.esine.nimi}!")
            self.sijainti.esine = None
        else:
            print("Täällä ei ole mitään.")


#Seivaus
def tallenna_peli(pelaaja, roskikset):
    with open(kansio / "save.txt", "w", encoding="utf-8") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(pelaaja.sijainti.nimi + "\n")

        tiedosto.write(",".join(str(roskis) for roskis in roskikset) + "\n")

        for esine in pelaaja.reppu:
            tiedosto.write(f"{esine.nimi};{esine.paino};{esine.arvo}\n")

    print("Peli tallennettu!")


#Lataus
def lataa_peli(pelaaja, piritori, puisto, roskikset):
    try:
        with open(kansio / "save.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.readlines()

        pelaaja.nimi = rivit[0].strip()

        sijainti = rivit[1].strip()

        if sijainti == "Piritori":
            pelaaja.sijainti = piritori

        elif sijainti == "Puisto":
            pelaaja.sijainti = puisto


        # Ladataan roskisten tila

        tallennetut_roskikset = rivit[2].strip().split(",")

        for i in range(3):
            roskikset[i] = tallennetut_roskikset[i] == "True"


        # Ladataan reppu

        pelaaja.reppu = []

        for rivi in rivit[3:]:
            tiedot = rivi.strip().split(";")

            nimi = tiedot[0]
            paino = float(tiedot[1])
            arvo = float(tiedot[2])

            esine = Esine(nimi, paino, arvo)
            pelaaja.reppu.append(esine)

        # Palautetaan Piritorin alkuperäinen tila ensin
        piritori.esine = Esine("Lääkeruisku", 0.1)

        # Jos ruisku on jo repussa, sitä ei saa uudestaan

        for esine in pelaaja.reppu:
            if esine.nimi == "Lääkeruisku":
                piritori.esine = None


        print("Peli ladattu!")
        print(f"Tervetuloa takaisin {pelaaja.nimi}!")
        print(f"Olet paikassa {pelaaja.sijainti.nimi}")
        print(pelaaja.sijainti.kuva)

        return True

    except FileNotFoundError:
        print("Tallennusta ei löytynyt.")
        return False


#Kaikki muut funktiot
def nayta_reppu(reppu):
        if len(reppu) == 0:
            print("Reppu on tyhjä.")
        else:
            print("Repussa on:")
            for esine in reppu:
                print(esine.nimi)

def tutki(pelaaja, roskikset):
    print(f"Lähdit tutkimaan paikkaa {pelaaja.sijainti.nimi}.")

    if pelaaja.sijainti.nimi == "Puisto":
        tutki_roskis(pelaaja, roskikset)

    else:
        pelaaja.keraa_esine()

def tutki_roskis(pelaaja, roskikset):
    roskis = input("Minkä roskiksen tutkit? 1, 2 vai 3: ")

    if roskis not in ["1", "2", "3"]:
        print("Tuollaista roskista ei ole.")
        return

    numero = int(roskis) - 1

    if roskikset[numero] == True:
        print("Roskis on tyhjä.")

    else:
        roskikset[numero] = True

        loyto = random.choice([Esine("Tölkki", 0.02, 0.10), Esine("Pieni pullo", 0.05, 0.20), Esine("Iso pullo", 0.1, 0.45)])

        pelaaja.reppu.append(loyto)

        print(f"Löysit: {loyto.nimi}!")
        print(f"Sen pantti on {loyto.arvo:.2f} €")

def lue_tiedosto(nimi):
    try:
        with open(kansio / nimi, "r", encoding="utf-8") as tiedosto:
            print(tiedosto.read())

    except FileNotFoundError:
        print(f"Tiedostoa {nimi} ei löytynyt.")


#Visuaalit

piritori_kuva = r"""
    ===========================================
                     Piritori
    ===========================================
                          
 /----------------/------------------/--------------/|
/                /                  /              / |
|---------------|------------------|--------------|  |
|               |                  |              |  |
| []    []   [] |  [] [] [] [] []  |  []  []  []  |  |
|               |                  |              |  |
| []    []   [] |  []    []    []  |  []  []  []  |  |
|               |                  |              |  /
|  1   ___      |   2   ___        |   3  ___     | /
|______|_|______|_______| |________|______| |_____|/
        

___________________________________________________
 _________        ________
/________/|      /_______/|  
|       |        |       |   /------------------/|
                            /------------------/ |
                            |                 |  |
                            |      Hissit     |  |
                            |      Metroon    |  /
                            |                 | /
                            |_________________|/

__________________________________________________

 /-----------------------------------------------/|
/-----------------------------------------------/ |
|  __________________       S-Market            | |
|  |                |         _____             | |
|  |________________|         |   |             | /  
|_____________________________|___|_____________|/
            
"""
puisto_kuva = r"""
    ===================================
                  Puisto
    ===================================

_________________________________________________
|__|____|__|_|___|__|__|___|_|____|__|___|__|___| 
|_|___|___|___|___|___|___|____|_|__|___|_____|_|
                                     __
      /////                        _(__)_
        ________        ////      (_)__(_)
       /_______/|      _=_           ||
       |      |        |_|  1        ||
___________________________              /////
      .           .        \____________________
________________________ .      .        .
                        \________    .
    _=_                         |            .
    |_|  2    /\    ////        |      .
             /__\               \_______________
            /____\                        _=_
            /____\                        |_|  3
  ////      /____\         /////      
              ||                       /////
_________________________________________________
|__|____|__|_|___|__|__|___|_|____|__|___|__|___| 
|_|___|___|___|___|___|___|____|_|__|___|_____|_|
"""

#Peli alkaa:
# Peli alkaa

lue_tiedosto("intro.txt")
lue_tiedosto("ohjeet.txt")

ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")


else:

    # Esineet
    ruisku = Esine("Lääkeruisku", 0.1)

    # Huoneet
    piritori = Huone("Piritori", ruisku, piritori_kuva)
    puisto = Huone("Puisto", None, puisto_kuva)

    # Roskikset
    roskikset = [False, False, False]

    jatka = input("Haluatko jatkaa tallennettua peliä? k/e: ").lower()

    if jatka == "k":
        pelaaja = Pelaaja("", piritori)
        ladattu = lataa_peli(pelaaja, piritori, puisto, roskikset)

        if ladattu == False:
            nimi = input("Anna nimesi: ")
            pelaaja = Pelaaja(nimi, piritori)
            print(f"Tervetuloa peliin, {pelaaja.nimi}!")
            print(pelaaja.sijainti.kuva)

    else:
        nimi = input("Anna nimesi: ")
        pelaaja = Pelaaja(nimi, piritori)

        print(f"Tervetuloa peliin, {pelaaja.nimi}!")
        print(pelaaja.sijainti.kuva)

    komento = ""

    while komento != "lopeta": 
        print("\nPäävalikko")
        print("1. Näytä reppu")
        print("2. Tutki")
        print("3. Liiku")
        print("4. Tallenna peli")
        print("5. Lataa peli")
        print("6. Lopeta")

        komento = input("Anna komento: ").lower()

        if komento == "1":
            nayta_reppu(pelaaja.reppu)

        elif komento == "2":
            tutki(pelaaja, roskikset)

        elif komento == "3":
            paikka = input("Piritori vai puisto? ").lower()

            if paikka == "piritori":
                pelaaja.liiku(piritori)

            elif paikka == "puisto":
                pelaaja.liiku(puisto)

        elif komento == "4":
            tallenna_peli(pelaaja, roskikset)

        elif komento == "5":
            lataa_peli(pelaaja, piritori, puisto, roskikset)

        elif komento == "6":
            print("Peli suljetaan.")
            break

        else:
            print("Tuntematon komento.")

