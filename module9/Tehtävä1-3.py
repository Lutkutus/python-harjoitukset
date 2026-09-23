class Auto:
   
    def __init__(self, rekisteri, huippunopeus, tamhetknop = 0, kuljettu_matka = 2000):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.tamhetknop = tamhetknop
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        self.tamhetknop = self.tamhetknop + muutos

        if self.tamhetknop > self.huippunopeus:
            self.tamhetknop = self.huippunopeus

        if self.tamhetknop < 0:
            self.tamhetknop = 0

    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + self.tamhetknop * tunnit


auto1 = Auto("ABC-123", 142)

print(f"Auton 1 rekisterinumero on {auto1.rekisteri}. Sen huippunopeus on {auto1.huippunopeus} km/h. Auton tämän hetkinen nopeus on {auto1.tamhetknop} km/h ja se on kulkenut {auto1.kuljettu_matka} km")

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print(f"Auton nopeus on {auto1.tamhetknop} km/h.")

auto1.kulje(1.5)

print(f"Auto on kulkenut {auto1.kuljettu_matka} km.")
  
auto1.kiihdytä(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto1.tamhetknop} km/h.")
