class Pelaaja:
    
    def __init__(self, nimi, elämät=3, kolikot=0, pisteet=0):
        self.nimi = nimi
        self.elämät = elämät
        self.kolikot = kolikot
        self.pisteet = pisteet

pelaaja1 = Pelaaja("Mario")
    
print(f"Pelaajalla {pelaaja1.nimi} on elämiä {pelaaja1.elämät} ja hänellä on kolikoita {pelaaja1.kolikot} ja hänellä on pisteitä {pelaaja1.pisteet}")