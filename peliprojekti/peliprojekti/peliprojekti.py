
class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


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


def lisaa_esine(reppu):
    esine = input("Minkä esineen haluat lisätä reppuun? ")
    reppu.append(esine)
    print(f"{esine} lisättiin reppuun!")


def nayta_reppu(reppu):
    if len(reppu) == 0:
        print("Reppu on tyhjä.")
    else:
        print("Repussa on:")
        for esine in reppu:
            print(esine)


def tutki(pelaaja):
    print(f"Lähdit tutkimaan paikkaa {pelaaja.sijainti.nimi}.")
    pelaaja.keraa_esine()

#Visuaalit

piritori_kuva = """
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

#Peli alkaa:

ika = int(input("Anna ikäsi: "))

if ika < 12:
    print("Olet liian nuori pelaamaan tätä peliä.")

else:
    nimi = input("Anna nimesi: ")

#Esineet
    ruisku = Esine("Lääkeruisku", 0.1)
    pullo = Esine("Tyhjä pullo", 0.2)

#Huoneet
    piritori = Huone("Piritori", ruisku, piritori_kuva)
    puisto = Huone("Puisto", pullo, piritori_kuva)

#Pelaaja
    pelaaja = Pelaaja(nimi, piritori)

    print(f"Tervetuloa peliin, {pelaaja.nimi}!")
    print(pelaaja.sijainti.kuva)
    komento = ""

    while komento != "lopeta":
        print("\nPäävalikko")
        print("1. Lisää esine")
        print("2. Näytä reppu")
        print("3. Tutki")
        print("4. Liiku")
        print("5. Lopeta")

        komento = input("Anna komento: ").lower()

        if komento == "lisää esine":
            lisaa_esine(pelaaja.reppu)

        elif komento == "näytä reppu":
            nayta_reppu(pelaaja.reppu)

        elif komento == "tutki":
            tutki(pelaaja)

        elif komento == "liiku":
            paikka = input("Piritori vai puisto? ").lower()

            if paikka == "piritori":
                pelaaja.liiku(piritori)

            elif paikka == "puisto":
                pelaaja.liiku(puisto)

        elif komento == "lopeta":
            print("Peli suljetaan.")

        else:
            print("Tuntematon komento.")